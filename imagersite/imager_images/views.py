"""Views for images and albums."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from imager_images.models import Album, ImagerProfile, Photo


class AlbumView(LoginRequiredMixin, ListView):
    """Display album for user."""

    model = Album
    context_object_name = 'albums'
    template_name = 'imager_images/album.html'
    redirect_field_name = '/accounts/login'

    def get_queryset(self):
        """Request users profile."""
        return Album.objects.all()


class AlbumPhotoView(LoginRequiredMixin, DetailView):
    """Display album for user."""

    model = Album
    context_object_name = 'photo'
    redirect_field_name = '/accounts/login'
    template_name = 'imager_images/albumphoto.html'

    def get_context_data(self, **kwargs):
        """Queryset of all photos in album."""
        photo = kwargs['object'].photo.filter(album=kwargs['object'].pk)
        context = super().get_context_data(**kwargs)
        context['photo'] = photo
        return context


@login_required(login_url='/accounts/login')
def library_view(request):
    """Callable view for the libraries."""
    user = ImagerProfile.objects.get(user=request.user)
    albums = Album.objects.filter(user=user).order_by('-date_uploaded')
    photos = Photo.objects.filter(user=user).order_by('-date_uploaded')
    return render(request, 'imager_images/library.html',
                  context={'photos': photos, 'albums': albums})


class PublicLibrary(LoginRequiredMixin, TemplateView):
    """Display album for user."""

    template_name = 'imager_images/library.html'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        """Request users profile."""
        # import pdb; pdb.set_trace()
        name = User.objects.get(username=kwargs['user'])
        user = ImagerProfile.objects.get(user=name)
        albums = Album.objects.filter(user=user)\
            .filter(published='PUBLIC').order_by('-date_uploaded')
        photos = Photo.objects.filter(user=user)\
            .filter(published='PUBLIC').order_by('-date_uploaded')
        context = super().get_context_data(**kwargs)
        context['photos'] = photos
        context['albums'] = albums
        return context


class PhotoListView(LoginRequiredMixin, ListView):
    """Class to display the photo list view."""

    context_object_name = 'photos'
    template_name = 'imager_images/photo.html'
    redirect_field_name = '/accounts/login'

    def get_queryset(self):
        """Get all photos from user."""
        return Photo.objects.all().filter(published='PUBLIC').\
            order_by('-date_uploaded')


class PhotoCreate(LoginRequiredMixin, CreateView):
    """Class based view to display form for uploading new photos."""

    model = Photo
    fields = [
        'docfile',
        'title',
        'description',
        'published',
        'date_published']
    template_name_suffix = '_create_form'
    redirect_field_name = '/accounts/login'

    def form_valid(self, form):
        """Validate form."""
        form_user = ImagerProfile.objects.get(user=self.request.user)
        form.instance.user = form_user
        return super(PhotoCreate, self).form_valid(form)


class AlbumCreate(LoginRequiredMixin, CreateView):
    """Class based view to display form for creating new albums."""

    model = Album
    fields = ['photo', 'cover', 'title', 'description',
              'published', 'date_published']
    template_name_suffix = '_create_form'
    redirect_field_name = '/accounts/login'

    def form_valid(self, form):
        """Validate form."""
        form_user = ImagerProfile.objects.get(user=self.request.user)
        form.instance.user = form_user
        return super(AlbumCreate, self).form_valid(form)


class PhotoUpdate(LoginRequiredMixin, UpdateView):
    """Class based view to display form for updating and editing photos."""

    model = Photo
    fields = [
        'docfile',
        'title',
        'description',
        'published',
        'date_published']
    template_name_suffix = '_update_form'
    context_object_name = 'photo'
    redirect_field_name = '/accounts/login'

    def get_object(self, queryset=None):
        """Populate form."""
        obj = Photo.objects.get(pk=self.kwargs['pk'])
        return obj


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    """Album update view."""

    model = Album
    fields = [
        'photo',
        'cover',
        'title',
        'description',
        'published',
        'date_published']
    template_name = 'imager_images/album_update_form.html'
    context_object_name = 'album'
    redirect_field_name = '/accounts/login'

    def get_object(self, queryset=None):
        """Populate form."""
        obj = Album.objects.get(pk=self.kwargs['pk'])
        return obj
