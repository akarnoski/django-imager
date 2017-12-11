"""Imager api views."""
from imager_api.serializers import PhotoSerializer

from imager_images.models import Photo

from rest_framework import generics, mixins


class ApiPhotoView(mixins.ListModelMixin,
                   generics.GenericAPIView):
    """Api view."""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        """Define api get request."""
        return self.list(request, *args, **kwargs)


# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

# from imager_api.serializers import PhotoSerializer

# from imager_images.models import Photo

# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer

# @csrf_exempt
# def photo_detail(request, pk):
#     """Retrieve, update or delete a photo."""
#     try:
#         photo = Photo.objects.get(pk=pk)
#     except Photo.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = PhotoSerializer(photo)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PhotoSerializer(photo, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         photo.delete()
#         return HttpResponse(status=204)
