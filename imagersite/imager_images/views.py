from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView

from imager_images.models import Album, ImagerProfile, Photo
from imager_images.forms import DocumentForm, AlbumForm


class AlbumView(ListView):
    """Display album for user."""

    model = Album
    context_object_name = 'albums'
    template_name = 'imager_images/album.html'

    def get_queryset(self):
        """Request users profile."""
        user = ImagerProfile.objects.get(user=self.request.user)
        return Album.objects.filter(user=user)


# def album_view(request):
#     """View to create albums."""
#     if number is None:
#         return render(request, 'imager_images/album.html')
#     else:
#         return render(request, 'imager_images/album.html', context={'photo_id': number})


def library_view(request):
    """Callable view for the libraaries."""
    # param_value = request.GET('username')
    return render(request, 'imager_images/library.html')


def photo_view(request, number=None):
    """Callable view for the libraaries."""
    if number is None:
        return render(request, 'imager_images/photo.html')
    else:
        return render(request, 'imager_images/photo.html', context={'photo_id': number})


class PhotoListView(ListView):
    """Class to display the photo list view."""
    context_object_name = 'photos'
    template_name = 'imager_images/photo.html'

    def get_queryset(self):
        profile = ImagerProfile.objects.get(user=self.request.user)
        return Photo.objects.filter(user=profile)
