from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Provide CRUD to any Admin users.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == request.user.is_staff
