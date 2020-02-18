"""Package model."""

# Django
from django.db import models

# Utilities
from utils.models import TrackingModel

class Package(TrackingModel):
    """Package model."""

    description = models.CharField('package description', max_length=255)
    is_fragile = models.BooleanField(default=False)
    weight = models.CharField('package weight', max_length=50)

    def __str__(self):
        """Return Package pk."""
        return self.pk

    class Meta:
        """Meta class."""
        ordering = ['-pk']