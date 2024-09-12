from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from apps.users.forms.users_form import CustomAuthenticationForm
from apps.users.views import UserListView, UserEditView, RegisterView, CustomPasswordResetView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='edit_user'),
    path('register/', RegisterView.as_view(), name='register'),
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
