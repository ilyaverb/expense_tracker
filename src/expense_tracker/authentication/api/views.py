from rest_framework import generics

from expense_tracker.authentication.api.serializers import ProfileSerializer
from expense_tracker.authentication.models import Profile
from expense_tracker.core.api.permissions import IsProfileOwner


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner, ]
    http_method_names = ['get', ]
    lookup_field = 'user__uid'

    def get_queryset(self):
        # return Profile.objects.all()
        return Profile.objects.all() if self.request.user.is_superuser else Profile.objects.filter(
            user=self.request.user)
