from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from expense_tracker.core.api.serializers import TransactionSerializer, CategorySerializer
from expense_tracker.core.api.permissions import IsOwner
from expense_tracker.core.api.mixins import PerformCreateMixin
from expense_tracker.core.api.filters import TransactionFilter
from expense_tracker.core.models import Transaction, Category


class TransactionViewSet(PerformCreateMixin, viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsOwner, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TransactionFilter
    ordering_fields = ['time', 'amount', 'date']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Transaction.objects.none()
        return Transaction.objects.filter(
            user=self.request.user) if not self.request.user.is_superuser else Transaction.objects.all()


class CategoryViewSet(PerformCreateMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsOwner, ]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Category.objects.none()
        return Category.objects.filter(
            user=self.request.user) if not self.request.user.is_superuser else Category.objects.all()
