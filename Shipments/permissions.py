"""User permissions."""

# Django rest framework
from rest_framework.permissions import BasePermission

class IsClientShipp(BasePermission):
    """Allow acces only to objecs owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj.user