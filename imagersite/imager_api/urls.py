"""Imager api urls."""
from django.conf.urls import url

from imager_api import views


urlpatterns = [
    url(r'^photos/$', views.ApiPhotoView.as_view()),
]
