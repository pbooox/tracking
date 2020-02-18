"""User permissions."""

# Django rest framework
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Allow acces only to admins users."""

    def has_permission(self, request, view):
        """Check user is admin."""
        return request.user.user_type == '1'
        