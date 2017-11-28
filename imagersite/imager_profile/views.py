from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from imager_profile.models import ImagerProfile
from imager_images.models import Photo
from imager_images.forms import AlbumForm, DocumentForm


def profile_view(request, username=None):
    if request.user.is_authenticated:
        request_user = User.objects.filter(username=request.user)
        profile = ImagerProfile.objects.get(user=request_user)
        return render(request, 'imagersite/profiles.html', context={'profile': profile})
