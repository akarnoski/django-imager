from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from imager_images.views import AlbumView, AlbumPhotoView, PublicLibrary

from imager_images import views
from imager_images.views import PhotoListView

app_name = 'imager_images'
urlpatterns = [
    url(r'^album$', AlbumView.as_view(), name='album'),
    url(r'^album/(?P<pk>\d+)', AlbumPhotoView.as_view(), name='albumphoto'),
    url(r'^photos', PhotoListView.as_view(), name='photo'),
    url(r'^library$', views.library_view, name='library'),
    url(r'^library/(?P<user>\w+)', PublicLibrary.as_view(), name='public_library'),
]
