from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from imager_images import views

urlpatterns = [
    url(r'^upload$', views.upload_view, name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)