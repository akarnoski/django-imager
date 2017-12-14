"""Models for images and albums."""
from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from imager_profile.models import ImagerProfile

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


class Photo(models.Model):
    """Create new photo model."""

    user = models.ForeignKey(
        ImagerProfile,
        related_name='photo',
        on_delete=models.CASCADE)
    highlighted = models.TextField(null=True)
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

    def __str__(self):
        """Render as string."""
        return self.title


class Album(models.Model):
    """Create new album model."""

    user = models.ForeignKey(
        ImagerProfile,
        related_name='album',
        on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo, related_name='album')
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

    def __str__(self):
        """Render as string."""
        return self.title


@receiver(post_save, sender=Album)
def change_album_publication_status(instance, **kwargs):
    """Set publication date on albums."""
    if not instance.date_published and instance.status == 'published':
        instance.date_published = datetime.now()
        instance.save()


@receiver(post_save, sender=Photo)
def change_photo_publication_status(instance, **kwargs):
    """Set publication date on albums."""
    if not instance.date_published and instance.status == 'published':
        instance.date_published = datetime.now()
        instance.save()
