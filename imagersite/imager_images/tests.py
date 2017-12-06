"""Tests for image and albums."""
from datetime import datetime

from bs4 import BeautifulSoup as Soup

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse_lazy

import factory

from imager_images.models import Album, Photo

from imager_profile.models import ImagerProfile
from imager_profile.tests import UserFactory


class UserGenerator(factory.django.DjangoModelFactory):
    """Factory for creating test Users."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Sequence(lambda user: 'user{}'.format(user))
    email = factory.Sequence(lambda user: '{}@email.com'.format(user))


class PhotoGenerator(factory.django.DjangoModelFactory):
    """Generator for testing photos."""

    class Meta:
        """Model meta."""

        model = Photo

    title = factory.Sequence(lambda title: "photo{}".format(title))
    img = SimpleUploadedFile(
        name='header-bg.jpg',
        content=open('imagersite/static/header-bg.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    description = 'this is a picture'
    date_uploaded = datetime.strptime('2017, 10, 1', '%Y, %m, %d')
    date_modified = datetime.now()
    date_published = datetime.strptime('2017, 10, 5', '%Y, %m, %d')
    published = 'Public'


class AlbumGenerator(factory.django.DjangoModelFactory):
    """Generator to test albums."""

    class Meta:
        """Model meta."""

        model = Album

    title = factory.Sequence(lambda album: "album{}".format(album))
    cover = SimpleUploadedFile(
        name='map-image.jpg',
        content=open('imagersite/static/map-image.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    description = 'this is an album'
    date_uploaded = datetime.strptime('2017, 10, 1', '%Y, %m, %d')
    date_modified = datetime.now()
    date_published = datetime.strptime('2017, 10, 5', '%Y, %m, %d')
    published = 'Public'


class PhotoandAlbumTests(TestCase):
    """Test photo and album models."""

    def setup(self):
        """Set up test users, photos, and albums."""
        self.user = [UserGenerator.create() for x in range(10)]
        self.photos = [PhotoGenerator.create() for x in range(10)]
        self.user = [AlbumGenerator.create() for x in range(10)]

    def 