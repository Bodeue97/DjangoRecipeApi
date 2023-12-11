from rest_framework.permissions import BasePermission

class CanEditCategory(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.has_perm('recipesolver.add_category') and  
            request.user.has_perm('recipesolver.change_category') and  
            request.user.has_perm('recipesolver.delete_category')  
        )
