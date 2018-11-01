from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'password'
        )


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'password',
            'token'
        )
