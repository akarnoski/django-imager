"""Tests for image and albums."""
from datetime import datetime

from bs4 import BeautifulSoup as soup

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse_lazy

import factory

from imager_images.models import Album, Photo

from imager_profile.models import ImagerProfile


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
    # f = open('imagersite/static/img/header-bg.jpg', 'rb')
    docfile = SimpleUploadedFile(
        name='header-bg.jpg',
        content=open('imagersite/static/img/header-bg.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    description = 'this is a picture'
    date_uploaded = datetime.strptime('2017, 10, 1', '%Y, %m, %d')
    date_modified = datetime.now()
    date_published = datetime.strptime('2017, 10, 5', '%Y, %m, %d')
    published = 'PUBLIC'


class AlbumGenerator(factory.django.DjangoModelFactory):
    """Generator to test albums."""

    class Meta:
        """Model meta."""

        model = Album

    title = factory.Sequence(lambda album: "album{}".format(album))
    # f = open('imagersite/static/img/map-image.png', 'rb')
    cover = SimpleUploadedFile(
        name='map-image.jpg',
        content=open('imagersite/static/img/map-image.png', 'rb').read(),
        content_type='image/png'
    )
    description = 'this is an album'
    date_uploaded = datetime.strptime('2017, 10, 1', '%Y, %m, %d')
    date_modified = datetime.now()
    date_published = datetime.strptime('2017, 10, 5', '%Y, %m, %d')
    published = 'PUBLIC'


class PhotoandAlbumTests(TestCase):
    """Test photo and album models."""

    def setUp(self):
        """Set up test users, photos, and albums."""
        self.user = []
        self.photo = []
        self.album = []
        self.client = Client()
        for i in range(20):
            self.user.append(UserGenerator.create())
            photo = PhotoGenerator.build()
            album = AlbumGenerator.build()
            photo.user = self.user[-1].profile
            album.user = self.user[-1].profile
            photo.save()
            album.save()
            self.photo.append(photo)
            self.album.append(album)

    def test_user_is_active(self):
        """Test that user has been created."""
        self.assertTrue(self.user[0].is_active)

    def test_twenty_users_exist(self):
        """Test that all users were created."""
        self.assertEqual(len(self.user), 20)

    def test_twenty_photos_created(self):
        """Test that twenty photos were created."""
        self.assertEqual(len(self.photo), 20)

    def test_twenty_albums_created(self):
        """Test that twenty albumbs were created."""
        self.assertEqual(len(self.album), 20)

    def test_user_has_profile(self):
        """Test user has profile."""
        self.assertTrue(self.user[5].profile is not None)

    def test_user_and_album_user_equal(self):
        """Test the user and album user are the same."""
        self.assertEqual(self.user[0].username, str(self.photo[0].user))

    def test_album_and_photo_user_equal(self):
        """Test the album and photo objects have same user."""
        self.assertTrue(self.photo[10].user, self.album[10].user)

    def test_album_has_proper_title(self):
        """Test album cover photo is right photo."""
        self.assertTrue('album' in self.album[9].title)

    def test_photo_title_is_correct(self):
        """Test photo has title."""
        self.assertTrue('photo' in self.photo[8].title)

    def test_photo_description_correct(self):
        """Test photo has appropriate description."""
        self.assertEqual(self.photo[3].description, 'this is a picture')

    def test_album_description_correct(self):
        """Test album has appropriate description."""
        self.assertEqual(self.album[3].description, 'this is an album')

    def test_photo_is_jpg(self):
        """Test photo is jpg."""
        self.assertTrue(str(self.photo[3].docfile).split('.')[1] == 'jpg')

    def test_album_view_redirects_to_login(self):
        """Test request album view redirects to login page."""
        response = self.client.get(reverse_lazy('imager_images:album'),
                                   follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_photo_view_redirects_to_login(self):
        """Test request to photo view redirects to login page."""
        response = self.client.get(reverse_lazy('imager_images:photo'),
                                   follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_library_view_redirects_to_login(self):
        """Test library view redirectso to login page."""
        response = self.client.get(reverse_lazy('imager_images:library'),
                                   follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_album_view_after_login_uses_proper_template(self):
        """Test album view after login shows proper template."""
        user = self.user[1]
        user.set_password('letmeinplease')
        user.save()
        self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'letmeinplease'
            },
            follow=True
        )
        response = self.client.get(reverse_lazy('imager_images:album'))
        self.assertTemplateUsed(response, 'imager_images/album.html')

    def test_photo_view_after_login_uses_proper_template(self):
        """Test album view after login shows proper template."""
        user = self.user[1]
        user.set_password('letmeinplease')
        user.save()
        self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'letmeinplease'
            },
            follow=True
        )
        response = self.client.get(reverse_lazy('imager_images:photo'))
        self.assertTemplateUsed(response, 'imager_images/photo.html')

    def test_album_view_shows_an_actual_album(self):
        """Test album view shows an album title."""
        user = self.user[1]
        user.set_password('letmeinplease')
        user.save()
        self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'letmeinplease'
            },
            follow=True
        )
        response = self.client.get(reverse_lazy('imager_images:album'))
        html = soup(response.content, 'html.parser')
        description = html.find('p', {'class': 'text-muted'})
        self.assertIsNotNone(description)
        self.assertEqual(description.text, 'this is an album')

    def test_photo_view_shows_an_actual_photo(self):
        """Test photo view shows an photo title."""
        user = self.user[1]
        user.set_password('letmeinplease')
        user.save()
        self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'letmeinplease'
            },
            follow=True
        )
        response = self.client.get(reverse_lazy('imager_images:photo'))
        html = soup(response.content, 'html.parser')
        description = html.find('p')
        self.assertIsNotNone(description)
        self.assertEqual(description.text, 'this is a picture')

    def test_library_view_shows_only_users_content(self):
        """Test photo view shows an photo title."""
        user = self.user[1]
        user.set_password('letmeinplease')
        user.save()
        self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'letmeinplease'
            },
            follow=True
        )
        self.client.get(reverse_lazy('imager_images:library'))
        self.assertEqual(str(Photo.objects.filter(user=user.profile)[0].user),
                         user.username)

    def test_albumphoto_view_shows_only_photos_from_one_album(self):
        """Test photo view shows an photo title."""
        user = self.user[1]
        user.set_password('letmeinplease')
        user.save()
        self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'letmeinplease'
            },
            follow=True
        )
        self.client.get(reverse_lazy('imager_images:albumphoto'))
        import pdb; pdb.set_trace()
        self.assertEqual(str(Photo.objects.filter(user=user.profile)[0].user),
                         user.username)