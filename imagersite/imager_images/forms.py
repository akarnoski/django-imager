from django import forms
from datetime import datetime
from imager_images.models import Photo


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('docfile', 'title', 'description', 'published')
    # docfile = forms.ImageField(
    #     label='Select a file',
    #     help_text='max. 42 megabytes'
    # )
    # title = forms.CharField(label='Title', max_length=30)
    # description = forms.CharField(label='Description', widget=forms.Textarea)
    # PUBLISHED = [
    #     ('PRIVATE', 'Private'),
    #     ('SHARED', 'Shared'),
    #     ('PUBLIC', 'Public'),
    # ]
    # published = forms.ChoiceField(
    #     choices=PUBLISHED
    # )


class AlbumForm(forms.Form):
    title = forms.CharField(label='Title', max_length=30)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    # photo_options = forms.ModelMultipleChoiceField(queryset=Photo)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ]
    published = forms.ChoiceField(
        choices=PUBLISHED
    )
