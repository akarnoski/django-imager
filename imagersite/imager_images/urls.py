from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from imager_images import views

app_name = 'imager_images'
urlpatterns = [
    url(r'^photos', views.photo_view, name='photo'),
    url(r'^photos/(?P<number>\d+)', views.photo_view, name='photo'),
    url(r'^album$', views.album_view, name='album'),
    url(r'^album/(?P<number>\d+)', views.album_view, name='album'),
    url(r'^library', views.library_view, name='library'),

]