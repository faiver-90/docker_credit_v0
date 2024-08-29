from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('change-active-dealership/', change_active_dealership, name='change_active_dealership'),

    path('continue_docs/', ContinueDocsView.as_view(), name='continue_docs'),

    path('send_to_bank/', SendToBankView.as_view(), name='send_to_bank'),
    path('requests/<int:client_id>/', RequestOffersView.as_view(), name='client_offers'),

    path('user_upload/<int:pk>/', UserUploadDocumentView.as_view(), name='user_upload_document'),

    path('get-address-suggestions/', get_address_suggestions, name='get_address_suggestions'),

    path('upload/<int:pk>/', UploadDocumentView.as_view(), name='upload_document'),

    path('load_all_data_client/<int:pk>/', LoadAllDataClientView.as_view(), name='load_all_data_client'),
    path('manage_offers/', ManageSelectOffersView.as_view(), name='manage_select_offers'),
    path('offers/', OffersView.as_view(), name='offers'),
    path('get_card_offer/<int:offer_id>/', ShowSelectCardOfferView.as_view(), name='show_select_offers'),
    path('car-form/', QuestionnaireView.as_view(), name='car_form'),
    path('car-form/<int:pk>/', QuestionnaireView.as_view(), name='car_form'),
    path('', IndexView.as_view(), name='home'),

    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/edit/<int:pk>/', UserEditView.as_view(), name='edit_user'),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
