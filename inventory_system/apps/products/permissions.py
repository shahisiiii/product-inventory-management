"""Custom permissions for products."""

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allow read access to authenticated users, write access to admins only."""

    def has_permission(self, request, view):
        """Check user permission based on role."""
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == "ADMIN"
