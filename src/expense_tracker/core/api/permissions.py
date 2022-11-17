from rest_framework.permissions import IsAuthenticated


class IsOwner(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id or request.user.is_superuser


class IsProfileOwner(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id and view.kwargs.get(
            'user__uid') == request.user.uid or request.user.is_superuser
