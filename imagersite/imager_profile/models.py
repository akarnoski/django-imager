"""Models for imagersite."""
from django.contrib.auth.models import User
from django.db import models

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
    active = ProfileManager()
    email = models.CharField(max_length=100, blank=True)
    USERNAME_FIELD = 'email'
    phone = models.CharField(max_length=12, blank=False)
    website = models.URLField(blank=False)
    location = models.CharField(max_length=30, blank=False)
    fee = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
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

    @property
    def username(self):
        """Create username property."""
        return getattr(self, self.USERNAME_FIELD)

    @username.setter
    def set_username(self, value):
        """Create a setter for username."""
        self.email = value
