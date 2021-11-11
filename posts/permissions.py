from rest_framework import permissions


class IsStaffOrIsOwnerToDelete(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return bool(request.user.is_staff or obj.author.id == request.user.id)

        return True
