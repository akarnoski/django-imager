"""Imager api urls."""
from django.conf.urls import include, url

from imager_api import views

urlpatterns = [
    url(r'^$', views.ApiPhotoView.as_view()),
    # url(r'^api/(?P<pk>[0-9]+)/$', views.photo_detail),
]



# from django.conf.urls import include
# from imager_images.views import PhotoListView

# from rest_framework.routers import DefaultRouter
# from rest_framework import renderers


# photo_list = PhotoListView.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# photo_detail = PhotoListView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# photo_highlight = PhotoListView.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
