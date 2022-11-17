from django.contrib.auth import get_user_model

from rest_framework import viewsets

from expense_tracker.authentication.api.serializers import UserSerializer
from expense_tracker.authentication.api.permissions import IsSelf


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelf]
    lookup_field = 'uid'

    def get_queryset(self):
        return get_user_model().objects.all()
