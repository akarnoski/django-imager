from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from imager_images.models import Photo
from imager_images.forms import DocumentForm, AlbumForm


def album_view(request):
    """View to create albums."""
    if number is None:
        return render(request, 'imager_images/album.html')
    else:
        return render(request, 'imager_images/album.html', context={'photo_id': number})


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
