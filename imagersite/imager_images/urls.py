from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from imager_images import views

urlpatterns = [
    url(r'^upload$', views.upload_view, name='upload'),
    url(r'^album$', views.album_view, name='album'),
    url(r'^library', views.library_view, name='library'),

]