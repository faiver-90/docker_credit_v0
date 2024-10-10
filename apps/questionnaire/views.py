import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView

# from apps.common_services.kafka.kafka_service import KafkaProducerService

from .forms.upload_file_form import ClientUploadDocumentForm
from .models import ClientPreData, ClientDocument
from apps.users.models import Dealership
# from apps.core.log_storage.logging_servivce import custom_logger

from .services.dadata_service.cladr_service import CladrService
from .services.index_list_application_service import ApplicationService
from .services.offer_services.create_update_offers_in_db_service import CreateUpdateOffersInDbService
from .services.offer_services.get_offers_by_status import GetByStatusOfferService
from .services.offer_services.manage_select_offers_service import SelectedOfferService
from .services.offer_services.show_selected_offers_to_card import ShowOfferService
from .services.questionnaire.client_extra_data_service import ClientExtraDataService
from .services.questionnaire.questionnaire_view_services import QuestionnairePostHandler, QuestionnaireGetHandler
from .services.questionnaire.continue_docs_service import ContinueDocsService
from .services.upload_document_service import BaseUploadDocumentView
from apps.core.common_services.paginator_service import PaginationService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot import \
    SovcombankHandler, DataPreparationService, ValidationService
import logging

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, View):
    """Отображение всех созданных заявок"""
    per_page = 10

    def get(self, request):
        # Получение параметров из запроса
        ordering = request.GET.get('ordering', '-date_create_all_app')
        dealership_filter = request.GET.get('dealership', '')
        status_filter = request.GET.get('status', '')
        page_number = request.GET.get('page', 1)

        # Используем сервис для получения заявок с фильтрацией
        object_list = ApplicationService.get_applications(
            user=request.user,
            dealership_filter=dealership_filter,
            status_filter=status_filter,
            ordering=ordering
        )

        page_obj = PaginationService.paginate(object_list, page_number=page_number, per_page=self.per_page)

        field_labels = {
            'client': 'ФИО',
            'statuses': 'Статус',
            'type': 'Тип',
            'financing': 'Финансирование',
            'author': 'Автор',
            'dealership': 'Дилерский центр',
            'organization': 'Юридическое лицо',
            'date_create': 'Дата создания',
            'date_changes': 'Дата изменения',
        }

        # Отправляем данные в шаблон
        return render(request, 'questionnaire/index.html', {
            'applications': page_obj,
            'dealership_filter': dealership_filter,
            'status_filter': status_filter,
            'field_labels': field_labels
        })


class ChangeActiveDealershipView(LoginRequiredMixin, View):
    @staticmethod
    def post(request, *args, **kwargs):
        dealership_id = request.POST.get('active_dealership')
        if dealership_id:
            user_profile = request.user.userprofile
            try:
                dealership = user_profile.dealership_manager.get(id=dealership_id)
                user_profile.set_active_dealership(dealership)
            except Dealership.DoesNotExist as e:
                # custom_logger(e, 'error')
                return JsonResponse("Dealership does not exist.")

        return redirect(request.META.get('HTTP_REFERER', 'home'))


class ContinueDocsView(LoginRequiredMixin, View):
    """Перенаправление на страницу оформления заявки после одобрения"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        id_app_in_system = request.GET.get('id_app_in_system')

        service = ContinueDocsService()
        context = service.get_context_for_continue_fill(client_id=client_id,
                                                        id_app_in_system=id_app_in_system)

        return render(request, 'questionnaire/continue_docs.html', context)


class RequestOffersView(LoginRequiredMixin, ListView):
    """Формирование страницы с заявками"""
    template_name = 'questionnaire/requests.html'
    context_object_name = 'status_offers'

    def get_queryset(self):
        bank_offer_service = GetByStatusOfferService()
        client_id = self.kwargs['client_id']
        return bank_offer_service.get_offers_by_status(client_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_id'] = self.kwargs['client_id']
        context['offers_by_status'] = self.get_queryset()
        return context


# class SendToBankView(LoginRequiredMixin, View):
#     def post(self, request, *args, **kwargs):
#         # Выводим сообщение в консоль после нажатия на кнопку
#         print("Кнопка нажата! Сообщение записано в консоль.")
#         client_id = request.POST.get('client_id')
#         user = request.user
#         response_data = DataPreparationService().prepare_data(user, client_id)
#         ValidationService().validate(response_data)
#         return JsonResponse({'message': response_data}, json_dumps_params={'ensure_ascii': False, 'indent': 4})
class SendToBankView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            # Логика обработки запроса
            print("Кнопка нажата! Сообщение записано в консоль.")
            client_id = request.POST.get('client_id')
            user = request.user
            response_data = DataPreparationService().prepare_data(user, client_id)

            # Валидация данных
            ValidationService().validate(response_data)

            # Возвращаем успешный ответ
            return JsonResponse({'message': response_data}, json_dumps_params={'ensure_ascii': False, 'indent': 4})

        except Exception as e:
            # В случае ошибки возвращаем JSON с информацией об ошибке
            return JsonResponse({'error': str(e)}, status=400, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    # """Отправка заявки в банк"""
    # topic = 'database'
    # kafka_service = KafkaProducerService()
    # bank_offer_service = SendToBankService()
    #
    # def post(self, request, *args, **kwargs):
    #     client_id = request.POST.get('client_id')
    #     selected_offers = request.POST.getlist('selected_offers')
    #
    #     if selected_offers:
    #         data = self.bank_offer_service.prepare_selected_offer_data(client_id,
    #                                                                    selected_offers)
    #         self.kafka_service.send_to_kafka(data,
    #                                          self.topic,
    #                                          client_id)
    #
    #     converted_elected_offers = convert_str_list(selected_offers)
    #
    #     for _ in range(60):
    #         if self.bank_offer_service.check_if_saved(client_id, converted_elected_offers):
    #             return redirect(f'/questionnaire/requests/{client_id}/')
    #         time.sleep(1)
    #
    #     return handle_logger('Офферы не были сохранены за отведенное время.',
    #                          logger_error,
    #                          additional_info=f'Не сохраненные id - {converted_elected_offers}')


class LoadAllDataClientView(LoginRequiredMixin, View):
    """
    Загрузка форм доп. информации о клиенте
    """

    @staticmethod
    def get(request, pk):
        client = get_object_or_404(ClientPreData, pk=pk)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            service = ClientExtraDataService(client)
            context = service.get_client_context()
            html = render_to_string('questionnaire/all_data_client.html',
                                    context,
                                    request=request)
            return JsonResponse({'html': html})
        return HttpResponse(status=400)

    @staticmethod
    def post(request, pk):
        client = get_object_or_404(ClientPreData, id=pk)
        service = ClientExtraDataService(client)

        form_data = {key: request.POST.dict() for key in service.forms_map.keys()}
        forms = service.prepare_forms(form_data)

        ignore_required = request.POST.get('ignore_required', 'false') == 'true'
        if ignore_required:
            service.set_fields_not_required(forms)

        if all(form.is_valid() for form in forms.values()):
            service.save_forms(forms)
            return JsonResponse({'success': True})
        else:
            errors = {form.__class__.__name__: form.errors for form in forms.values()}
            return JsonResponse({'success': False, 'error': errors}, status=400)


class QuestionnaireView(LoginRequiredMixin, View):
    """Представление для обработки создания и редактирования заявки клиента."""
    template_name = 'questionnaire/car_form.html'

    def get(self, request, *args, **kwargs):
        client_id = kwargs.get('pk')
        id_app_in_system = request.GET.get('id_app_in_system')
        id_app_bank = request.GET.get('id_app_bank')
        get_handler = QuestionnaireGetHandler()
        user = request.user
        active_dealership = user.userprofile.get_active_dealership()
        dealership_name = active_dealership.name if active_dealership else None

        redirect, context = get_handler.handle(client_id,
                                               id_app_in_system,
                                               id_app_bank, user,
                                               dealership_name)
        if redirect:
            return redirect
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id')
        ignore_required = request.POST.get('ignore_required', 'false') == 'true'
        form_data = request.POST.dict()
        post_handler = QuestionnairePostHandler()
        result = post_handler.handle(client_id, form_data, ignore_required)

        if result.get('success'):
            return JsonResponse({'success': True})
        else:
            return render(request, self.template_name, result)


class ManageSelectOffersView(LoginRequiredMixin, View):
    """CRUD карточек выбранных оферов"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        if not client_id:
            return JsonResponse({'status': 'error', 'message': 'client_id is required'}, status=400)

        offers_data = SelectedOfferService.get_offers(client_id=client_id)
        return JsonResponse({'offers': offers_data})

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            client_id = data.get('client_id')
            offer_id = data.get('offer_id')
            total_loan_amount = data.get('total_loan_amount')

            if not client_id or not offer_id:
                return JsonResponse({'status': 'error', 'message': 'client_id and offer_id are required'}, status=400)

            result = SelectedOfferService.create_or_update_offer(
                client_id=client_id,
                offer_id=offer_id,
                total_loan_amount=total_loan_amount
            )
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': e}, status=400)

    @staticmethod
    def delete(request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            client_id = data.get('client_id')
            offer_id = data.get('offer_id')

            if not client_id or not offer_id:
                return JsonResponse({'status': 'error', 'message': 'client_id and offer_id are required'}, status=400)

            result = SelectedOfferService.delete_offer(client_id=client_id,
                                                       offer_id=offer_id)
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': e}, status=400)


class ShowSelectCardOfferView(LoginRequiredMixin, View):
    """Отрисовка выбираемых оферов в предварительных расчетах после нажатия Выбрать"""

    @staticmethod
    def get(request, offer_id):
        try:
            car_price = request.GET.get('car_price')
            initial_payment = request.GET.get('initial_payment')
            total_loan_amount = request.GET.get('total_loan_amount')

            context = ShowOfferService.get_offer_data(
                offer_id=offer_id,
                car_price=car_price,
                initial_payment=initial_payment,
                total_loan_amount=total_loan_amount
            )

            return render(request, 'questionnaire/card_offer.html', context)
        except Http404 as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


class CreateUpdateOffersInDbView(LoginRequiredMixin, View):
    """Отображение и создание в БД предложений партнеров"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        if not client_id:
            return JsonResponse({'error': 'client_id is required'}, status=400)

        offers_data = CreateUpdateOffersInDbService.get_client_offers(client_id=client_id)
        return JsonResponse({'offers': offers_data})

    @staticmethod
    def post(request):
        financing_term = request.POST.get('financing_term')
        client_id = request.POST.get('client_id')

        if not financing_term or not client_id:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)

        offers_html = CreateUpdateOffersInDbService.create_client_offers(client_id=client_id,
                                                                         financing_term=financing_term)

        return JsonResponse(offers_html, safe=False)


class UploadDocumentView(BaseUploadDocumentView):
    """Загрузка документов клиента в облако"""
    form_class = ClientUploadDocumentForm
    template_name = 'questionnaire/upload_document_client.html'
    document_model = ClientDocument
    client_user_field_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'documents': self.document_model.objects.filter(client_id=self.kwargs.get('pk')),
            'client_id': self.kwargs.get('pk')
        })
        return context

    def get_client_user(self):
        return get_object_or_404(ClientPreData, id=self.request.POST.get('client_id'))

    def delete(self, request, *args, **kwargs):
        try:
            document_id = json.loads(request.body).get('document_id')
            response = self.doc_service.delete_document(self.document_model, document_id)
            return response
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def get_address_suggestions(request):
    cladr_service = CladrService()
    query = request.GET.get('query', '')
    result = cladr_service.dadata_search(query)
    return JsonResponse(result)
