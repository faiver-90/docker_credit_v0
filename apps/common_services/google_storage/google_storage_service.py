import os
from datetime import timedelta

import requests
from django.http import JsonResponse
from google.cloud import storage

# Путь к вашему JSON файлу с ключом сервисного аккаунта
SERVICE_ACCOUNT_FILE = 'common_services/google_storage/credit_f902.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACCOUNT_FILE


def get_gsc_data(bucket_name, destination_blob_name=None):
    """Получение инстанса gsc"""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    return bucket.blob(destination_blob_name)


def generate_signed_url(bucket_name, destination_blob_name, expiration=timedelta(minutes=15)):
    """Генерация URL для сканов документов"""
    blob = get_gsc_data(bucket_name, destination_blob_name)

    url = blob.generate_signed_url(
        expiration=expiration,
        method='GET'
    )
    return url


def upload_to_bucket(bucket_name, file_content, destination_blob_name):
    """Загрузка скана в бакет"""
    blob = get_gsc_data(bucket_name, destination_blob_name)

    blob.upload_from_file(file_content)

    print(f"File uploaded to {destination_blob_name}.")


def delete_from_bucket(bucket_name, destination_blob_name):
    """Удаление файлы из бакета"""
    blob = get_gsc_data(bucket_name, destination_blob_name)

    if not blob.exists():
        print(f"Blob {destination_blob_name} does not exist.")
        return JsonResponse({'status': 'error', 'message': 'Файл не найден в Google Cloud Storage'}, status=404)

    blob.delete()

    print(f"Blob {destination_blob_name} deleted.")


def send_file_directly_from_bucket(api_url, bucket_name, destination_blob_name):
    """Отправляет файл напрямую из Google Cloud Storage по API"""
    blob = get_gsc_data(bucket_name, destination_blob_name)

    # Получаем потоковый объект файла
    with blob.open("rb") as blob_data:
        files = {'file': (destination_blob_name, blob_data)}
        response = requests.post(api_url, files=files)
        return response


def delete_folder(bucket_name, folder_name):
    """Удаление папки из бакета"""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=folder_name)
    for blob in blobs:
        blob.delete()
        print(f"Blob {blob.name} deleted.")
