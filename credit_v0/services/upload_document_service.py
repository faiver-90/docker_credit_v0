from django.http import JsonResponse
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter
from django.shortcuts import get_object_or_404

from app_v0 import settings
from credit_v0.services.google_storage.google_storage_service import upload_to_bucket, delete_from_bucket, \
    generate_signed_url


class DocumentService:
    ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/tiff']
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    def handle_files(self, files):
        documents = []
        images = []
        for f in files:
            if f.size > self.MAX_FILE_SIZE:
                return None, None, JsonResponse(
                    {'status': 'error', 'message': f'Файл слишком большой: {f.name}. Максимум 5мб.'})
            if f.content_type == 'application/pdf':
                documents.append(f)
            elif f.content_type in self.ALLOWED_IMAGE_TYPES:
                try:
                    image = Image.open(f)
                    image = image.convert('RGB')
                    images.append(image)
                except Exception as e:
                    return None, None, JsonResponse(
                        {'status': 'error', 'message': f'Error processing file {f.name}: {e}'})
            else:
                return None, None, JsonResponse({'status': 'error',
                                                 'message': f'Неверный формат файла: {f.content_type}. '
                                                            f'Доступные форматы {self.ALLOWED_IMAGE_TYPES}'})

        return documents, images, None

    def process_upload(self, form, document_model, client_user_field_name, client):
        document_type = form.cleaned_data['document_type']
        files = form.cleaned_data['document_files']

        filter_kwargs = {f"{client_user_field_name}": client, 'document_type': document_type}
        if document_model.objects.filter(**filter_kwargs).exists():
            # Возвращаем JSON с ошибкой вместо HTML
            return JsonResponse({'status': 'error', 'message': 'Документ с таким типом уже существует.'})

        documents, images, error_response = self.handle_files(files)
        if error_response:
            return error_response

        merged_pdf_name, pdf_content = self.save_pdf(documents, images, f'{client.id}_{document_type}')

        # Генерация пути для хранения файла в GCS
        folder_path = f'{client_user_field_name}_documents/{client_user_field_name}_{client.id}'
        destination_blob_name = f'{folder_path}/{merged_pdf_name}'

        # Загрузка файла в Google Cloud Storage
        self.upload_document_to_gcs(pdf_content, destination_blob_name)

        document_kwargs = {client_user_field_name: client, 'document_type': document_type}
        document = document_model(**document_kwargs)
        document.document_file = destination_blob_name  # Сохраняем путь к файлу в поле модели как строку
        document.save()

        return JsonResponse({'status': 'success', 'message': f'{document_type} загружены успешно'})

    @staticmethod
    def save_pdf(documents, images, name_prefix):
        pdf_io = BytesIO()

        # Объединение PDF файлов
        if documents:
            merger = PdfMerger()
            for doc in documents:
                merger.append(doc)
            merger.write(pdf_io)
            merger.close()

        # Конвертирование и добавление изображений
        if images:
            if documents:
                pdf_io.seek(0)
                existing_pdf = PdfFileReader(pdf_io)
                output_pdf = PdfFileWriter()
                for page_num in range(existing_pdf.getNumPages()):
                    output_pdf.addPage(existing_pdf.getPage(page_num))
                for image in images:
                    img_pdf = BytesIO()
                    image.save(img_pdf, format='PDF')
                    img_pdf.seek(0)
                    img_reader = PdfFileReader(img_pdf)
                    output_pdf.addPage(img_reader.getPage(0))
                pdf_io = BytesIO()
                output_pdf.write(pdf_io)
            else:
                images[0].save(pdf_io, save_all=True, append_images=images[1:], format='PDF')

        pdf_io.seek(0)
        merged_pdf_name = f'{name_prefix}.pdf'
        return merged_pdf_name, pdf_io.getvalue()

    @staticmethod
    def upload_document_to_gcs(pdf_content, destination_blob_name):
        bucket_name = settings.GOOGLE_CLOUD_STORAGE_BUCKET_NAME
        upload_to_bucket(bucket_name, BytesIO(pdf_content), destination_blob_name)


    def delete_document(self, document_model, document_id):
        try:
            document = get_object_or_404(document_model, id=document_id)
            bucket_name = settings.GOOGLE_CLOUD_STORAGE_BUCKET_NAME
            blob_name = str(document.document_file)  # Преобразуем объект FieldFile в строку

            # Удаление файла из Google Cloud Storage
            delete_from_bucket(bucket_name, blob_name)

            # Удаление записи из базы данных
            document.delete()
            return JsonResponse({'status': 'success', 'message': 'Документ успешно удален!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    @staticmethod
    def generate_signed_urls(documents):
        for document in documents:
            document.signed_url = generate_signed_url(
                settings.GOOGLE_CLOUD_STORAGE_BUCKET_NAME,
                document.document_file.name
            )
        return documents
