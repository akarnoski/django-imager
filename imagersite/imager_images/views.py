from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from imager_images.models import Photo
from imager_images.forms import DocumentForm, AlbumForm


def album_view(request):
    """View to create albums."""
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('imager_images.views.album_view'))
    else:
        form = AlbumForm()

    return render(
        request,
        'imager_images/album.html',
        context={'form': form}
    )


def library_view(request):
    """Callable view for the libraaries."""
    param_value = request.GET('username')
    return render(request, 'imager_images/library.html')


def photo_view(request, number=None):
    """Callable view for the libraaries."""
    if number is None:
        return render(request, 'imager_images/photo.html')
    else:
        return render(request, 'imager_images/photo.html', context={'photo_id': number})