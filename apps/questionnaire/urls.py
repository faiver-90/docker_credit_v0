from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from apps.questionnaire.views import ChangeActiveDealershipView, ContinueDocsView, SendToBankView, RequestOffersView, \
    get_address_suggestions, UploadDocumentView, LoadAllDataClientView, ManageSelectOffersView, \
    CreateUpdateOffersInDbView, ShowSelectCardOfferView, QuestionnaireView, IndexView

urlpatterns = [
    path('change_active_dealership/', ChangeActiveDealershipView.as_view(), name='change_active_dealership'),

    path('continue_docs/', ContinueDocsView.as_view(), name='continue_docs'),

    path('send_to_bank/', SendToBankView.as_view(), name='send_to_bank'),
    path('requests/<int:client_id>/', RequestOffersView.as_view(), name='client_offers'),

    path('get-address-suggestions/', get_address_suggestions, name='get_address_suggestions'),

    path('upload/<int:pk>/', UploadDocumentView.as_view(), name='upload_document'),

    path('load_all_data_client/<int:pk>/', LoadAllDataClientView.as_view(), name='load_all_data_client'),
    path('manage_offers/', ManageSelectOffersView.as_view(), name='manage_select_offers'),
    path('offers/', CreateUpdateOffersInDbView.as_view(), name='offers'),
    path('get_card_offer/<int:offer_id>/', ShowSelectCardOfferView.as_view(), name='show_select_offers'),
    path('car-form/', QuestionnaireView.as_view(), name='car_form'),
    path('car-form/<int:pk>/', QuestionnaireView.as_view(), name='car_form'),
    path('', IndexView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)