"""Shipment model."""

# Django
from django.db import models

# Utilities
from utils.models import TrackingModel

class Shipment(TrackingModel):
    """Shippment model"""
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    price = models.FloatField(default=50.0)

    STATE_CHOICES = [
        ('1', 'Warehouse'),
        ('2', 'Going'),
        ('3', 'Delivered'),
    ]

    state = models.CharField(max_length=1, choices=STATE_CHOICES, default=1)

    location = models.CharField(max_length=100, null=True, blank=True)

    packages = models.ManyToManyField(
        'packages.Package',
        through='Shipments.Shipment_detail',
    )

    def __str__(self):
        """Return shipment."""
        return "@{}'s shipment. #{}".format(
            self.user.username,
            self.shipment.pk,
        )
