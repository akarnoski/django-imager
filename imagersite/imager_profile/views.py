"""Views for imager profile."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import UpdateView

from imager_images.models import Photo

from imager_profile.models import ImagerProfile


@login_required(login_url='/accounts/login/')
def profile_view(request, username=None):
    """Request for profile view."""
    if username is None and request.user.is_authenticated:
        request_user = User.objects.filter(username=request.user)
        profile = ImagerProfile.objects.get(user=request_user)
        image_query = Photo.objects.filter(user=profile)
        image_count = image_query.count()
        return render(request, 'imager_profile/profiles.html',
                               context={'profile': profile,
                                        'image_count': image_count})
    else:
        request_user = User.objects.filter(username=username)
        profile = ImagerProfile.objects.get(user=request_user)
        return render(request, 'imager_profile/profiles.html',
                               context={'profile': profile})


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Class based to view to generate for user to update profile."""

    model = ImagerProfile
    fields = [
        'first_name',
        'last_name',
        'phone',
        'website',
        'location',
        'fee',
        'camera',
        'services',
        'bio',
        'photo_styles']
    template_name_suffix = '_update_form'
    context_object_name = 'profile'
    redirect_field_name = '/accounts/login'

    def get_object(self):
        """Populate form."""
        return self.request.user.profile


class UserUpdate(LoginRequiredMixin, UpdateView):
    """Update user information view."""

    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
    ]
    template_name = 'imager_profile/user_update_form.html'
    context_object_name = 'user'
    redirect_field_name = '/accounts/login'

    def get_object(self):
        """Fill form data."""
        return self.request.user
