from rest_framework.permissions import BasePermission


class IsHost(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "userprofile") and request.user.userprofile.role == "Host"


class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "userprofile") and request.user.userprofile.role == "Guest"