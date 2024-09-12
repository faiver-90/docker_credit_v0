from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from users.views import IndexView

urlpatterns = [
    path('new/', IndexView.as_view(), name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
