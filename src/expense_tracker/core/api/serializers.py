from rest_framework import serializers

from expense_tracker.core.models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='uid', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'date', 'time', 'description', 'category', 'organization', 'type', 'user')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='uid', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'user')
        extra_kwargs = {
            'id': {'read_only': True},
        }
