from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from imager_images.models import Photo
from imager_images.forms import DocumentForm, AlbumForm


def upload_view(request):
    """View for displaying the form for users to upload photos."""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('upload_view', current_app='imager_images', args=()))
    else:
        form = DocumentForm()
    documents = Photo.objects.all()

    return render(
        request,
        'imager_images/upload.html',
        context={'documents': documents, 'form': form}
    )


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
    return render(request, 'imager_images/photo.html', context={'photo_id': number})
