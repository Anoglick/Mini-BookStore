def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name='Moderator').exists()) 

def is_user(user):
        return user.groups.filter(name='User').exists()
