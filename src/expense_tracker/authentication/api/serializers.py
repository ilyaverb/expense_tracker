from django.contrib.auth import get_user_model

from rest_framework import serializers

from expense_tracker.authentication.models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'uid')
        extra_kwargs = {
            'uid': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='uid', read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'balance')
