"""Shipment model."""

# Django
from django.db import models

# Utilities
from utils.models import TrackingModel

class Shipment_detail(TrackingModel):
    """Shippment_detail model"""

    shipment = models.ForeignKey('Shipments.Shipment', on_delete=models.CASCADE)
    package = models.ForeignKey('packages.Package', on_delete=models.CASCADE)

    def __str__(self):
        """Return username and circle."""
        return 'Shipment #{} whith package #{}'.format(
            self.shipment.pk,
            self.package.pk,
        )