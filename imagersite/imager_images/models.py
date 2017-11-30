from django.db import models
from imager_profile.models import ImagerProfile
from multiselectfield import MultiSelectField

# Create your models here.


class Photo(models.Model):
    """Create new photo model."""

    user = models.ForeignKey(
        ImagerProfile,
        related_name='photo')
    docfile = models.ImageField(upload_to='images')
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ]
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED,
        blank=True
    )


class Album(models.Model):
    """Create new album model."""

    user = models.ForeignKey(
        ImagerProfile,
        related_name='album')
    photo = models.ManyToManyField(Photo)
    cover = models.ImageField(upload_to='cover-image')
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ]
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED,
        blank=True
    )
