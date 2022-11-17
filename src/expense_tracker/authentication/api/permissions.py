from rest_framework.permissions import IsAuthenticated


class IsSelf(IsAuthenticated):

    def has_permission(self, request, view):
        return view.action == 'create' or (
            request.user.is_superuser if view.action == 'list' else super().has_permission(
                request, view))

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_superuser
