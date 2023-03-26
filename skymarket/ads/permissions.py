from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(permissions.BasePermission):
    message = "Только владелец может изменить или удалить что-то в этой сущности"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.is_admin:
            return True
        return False