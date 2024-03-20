from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from users.models import User


class UserRegisterSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField()

    def validate(self, attrs):
        super().validate(attrs)
        password = attrs['password']
        request = self.context['request']
        password_confirmation = request.data['password_confirmation']
        if password != password_confirmation:
            raise ValidationError("The password does not match") # we should do this check on FE to avoid additional request
        validate_password(password)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
