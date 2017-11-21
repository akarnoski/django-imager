from imager_profile.models import ImagerProfile, User
from django.test import TestCase
import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """Class that inherits from factory."""
    class Meta:
        model = User
    username = 'bob'
    email = 'bob@example.com'


class ProfileTest(TestCase):

    def setUp(self):
        profile = ImagerProfile(website='nowhere')
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()
        profile.user = self.user
        profile.save()

    def test_one_user(self):
        one_user = User.objects.get()
        self.assertIsNotNone(one_user.profile)
