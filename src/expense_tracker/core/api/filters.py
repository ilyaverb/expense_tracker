from django_filters.rest_framework import FilterSet, TimeFilter, DateFilter, NumberFilter

from expense_tracker.core.models import Transaction


class TransactionFilter(FilterSet):
    time_after = TimeFilter(field_name='time', lookup_expr='gt')
    time_before = TimeFilter(field_name='time', lookup_expr='lt')
    date_from = DateFilter(field_name='date', lookup_expr='gt')
    date_to = DateFilter(field_name='date', lookup_expr='lt')
    amount_from = NumberFilter(field_name='amount', lookup_expr='gt')
    amount_to = NumberFilter(field_name='amount', lookup_expr='lt')

    class Meta:
        model = Transaction
        fields = ('time', 'amount', 'date')
