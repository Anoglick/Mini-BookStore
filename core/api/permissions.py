from rest_framework.permissions import BasePermission, IsAdminUser

class isAdminOrModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name='Moderator').exists()) 
    
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='User').exists()