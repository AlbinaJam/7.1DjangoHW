from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class OwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator:
            return request.user and request.user.is_superuser
        return True


class Draft(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.status == "DRAFT":
            return request.user == obj.creator
        return True
