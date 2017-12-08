"""Urls for imager images."""
from django.conf.urls import url

from imager_images import views
from imager_images.views import (
    AlbumCreate,
    AlbumPhotoView,
    AlbumUpdate,
    AlbumView,
    PhotoCreate,
    PhotoListView,
    PhotoUpdate,
    PublicLibrary)


app_name = 'imager_images'

urlpatterns = [
    url(r'^photos/add', PhotoCreate.as_view(success_url="images/library"),
        name='photoupload'),
    url(r'^photos/(?P<pk>\d+)/edit',
        PhotoUpdate.as_view(success_url="images/library"), name='photoedit'),
    url(r'^album/(?P<pk>\d+)/edit',
        AlbumUpdate.as_view(success_url="../../library"),
        name='albumedit'),
    url(r'^album/add', AlbumCreate.as_view(success_url="../../images/library"),
        name='albumupload'),
    url(r'^album$', AlbumView.as_view(), name='album'),
    url(r'^album/(?P<pk>\d+)', AlbumPhotoView.as_view(), name='albumphoto'),
    url(r'^photos', PhotoListView.as_view(), name='photo'),
    url(r'^library$', views.library_view, name='library'),
    url(r'^library/(?P<user>\w+)', PublicLibrary.as_view(),
        name='public_library'),
]
