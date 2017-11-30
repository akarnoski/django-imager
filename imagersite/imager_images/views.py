from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

from imager_images.models import Photo
from imager_profile.models import ImagerProfile


def album_view(request):
    """View to create albums."""
    if number is None:
        return render(request, 'imager_images/album.html')
    else:
        return render(request, 'imager_images/album.html', context={'photo_id': number})


def library_view(request):
    """Callable view for the libraaries."""
    photos = Photo.objects.all().filter(published='PUBLIC').order_by('-date_uploaded')
    return render(request, 'imager_images/library.html', context={'photos': photos})


class PhotoListView(ListView):
    """Class to display the photo list view."""
    context_object_name = 'photos'
    template_name = 'imager_images/photo.html'

    def get_queryset(self):
        # profile = ImagerProfile.objects.get(user=self.request.user)
        # return Photo.objects.filter(user=profile)
        return Photo.objects.all().filter(published='PUBLIC').order_by('-date_uploaded')
