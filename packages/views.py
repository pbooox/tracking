"""Packages views."""

# Django rest framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin

# Serializers
from packages.serializers import PackageModelSerializer


# Models
from packages.models import Package


class PackageViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
    ):
    """Package view set"""

    queryset = Package.objects.all()
    serializer_class = PackageModelSerializer
    
    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ['create', 'list', 'update', 'partial_update', 'retrieve']:
            permissions.append(IsAdmin)
        return [permission() for permission in permissions]
