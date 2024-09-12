from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from apps.users.views import UserListView, UserEditView, RegisterView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='edit_user'),
    path('register/', RegisterView.as_view(), name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
