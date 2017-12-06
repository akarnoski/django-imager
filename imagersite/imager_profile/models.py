"""Models for imagersite."""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField


class ProfileManager(models.Manager):
    """Redefine profile manager settings."""

    def get_queryset(self):
        """Redefine get_queryset is_active."""
        return super().get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Create a new imager profile."""

    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE)

    objects = models.Manager()
    active = ProfileManager()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    fee = models.DecimalField(decimal_places=2, max_digits=6,
                              blank=True, null=True)
    CAMERAS = [
        ('CANON', 'Canon'),
        ('NIKON', 'Nikon'),
        ('SONY', 'Sony'),
        ('FUJIFILM', 'Fujifilm')
    ]
    camera = MultiSelectField(
        max_choices=1,
        choices=CAMERAS,
        blank=True
    )
    SERVICES = [
        ('WEDDINGS', 'Weddings'),
        ('SCHOOL', 'School'),
        ('FAMILY', 'Family'),
        ('BABIES', 'Babies'),
        ('NATURE', 'Nature'),
        ('ABSTACT', 'Abstract'),
        ('OTHER', 'Other')
    ]
    services = MultiSelectField(
        max_choices=7,
        choices=SERVICES,
        blank=True
    )
    bio = models.TextField(blank=True)
    PHOTO_STYLES = [
        ('BW', 'Black and white'),
        ('COLOR', 'Color'),
        ('STILL', 'Still'),
        ('ACTION', 'Action'),
    ]
    photo_styles = MultiSelectField(
        max_choices=4,
        choices=PHOTO_STYLES,
        blank=True
    )

    @property
    def is_active(self):
        """Create property is_active for model."""
        return self.user.is_active

    def __repr__(self):
        """Make me a string."""
        return self.user.username

    def __str__(self):
        """Render name as string."""
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """Automatically create profile when user is created."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
