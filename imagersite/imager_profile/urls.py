from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from imager_profile import views

app_name = 'imager_profile'
urlpatterns = [
    url(r'^edit', views.ProfileUpdate.as_view(success_url="/profile"), name='profileupdate'),
    url(r'^$', views.profile_view, name='user_profile'),
    url(r'^(?P<username>\w+)', views.profile_view, name='profile'),
]
