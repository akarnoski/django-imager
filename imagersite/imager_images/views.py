from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from imager_images.models import Photo
from imager_images.forms import DocumentForm


def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Photo(docfile=request.FILES['docfile'])
            newdoc.save()
            # return HttpResponseRedirect(reverse('imager_images.views.list'))
    else:
        form = DocumentForm()
    documents = Photo.objects.all()

    return render(
        request,
        'imager_images/index.html',
        context={'documents': documents, 'form': form}
    )
