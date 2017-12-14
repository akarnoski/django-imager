"""Imager api views."""
from imager_api.serializers import PhotoSerializer

from imager_images.models import Photo

from imager_profile.models import ImagerProfile

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ApiPhotoView(generics.ListAPIView):
    """Api view."""

    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Refine query return."""
        user = ImagerProfile.objects.get(user=self.request.user)
        queryset = Photo.objects.filter(user=user)
        return queryset
