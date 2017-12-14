"""Serialization of photo class."""
from imager_images.models import Photo

from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    """Serialize the photo model."""

    class Meta:
        """Serialize all fields."""

        model = Photo
        fields = ('id', 'user', 'title', 'docfile', 'description',
                  'date_uploaded', 'date_modified', 'date_published',
                  'published')
