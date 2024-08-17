from rest_framework import permissions


class CustomPermissions(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.method in ['PATCH', 'PUT']:
                return True

            if request.method == 'DELETE' and request.user.is_superuser:
                return True


        return False
