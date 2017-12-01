from django import forms
from datetime import datetime
from imager_images.models import Photo


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('docfile', 'title', 'description', 'published')


