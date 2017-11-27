from django.db import models
from imager_profile.models import ImagerProfile
from multiselectfield import MultiSelectField

# Create your models here.


class Photo(models.Model):
    """Create new photo model."""

    user = models.OneToOneField(
        ImagerProfile,
        related_name='photo')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ]
    published = MultiSelectField(
        max_choices=1,
        choices=PUBLISHED,
        blank=True
    )


class Album(models.Model):
    """Create new album model."""

    user = models.OneToOneField(
        ImagerProfile,
        related_name='album')
    photo = models.ManyToManyField(Photo)
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ]
    published = MultiSelectField(
        max_choices=1,
        choices=PUBLISHED,
        blank=True
    )