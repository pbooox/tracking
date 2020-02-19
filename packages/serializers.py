"""Package serializers."""

# Django rest framework
from rest_framework import serializers

# Model
from packages.models import Package


class PackageModelSerializer(serializers.ModelSerializer):
    """Package model serializer."""

    class Meta:
        """Meta class."""

        model = Package
        fields=(
            'id',
            'description',
            'is_fragile',
            'weight'
        )

    
