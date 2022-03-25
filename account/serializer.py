from rest_framework import serializers

from account.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    """ User serializer"""
    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.ModelSerializer):
    """ Login serializer"""
    id = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class LogoutSerializer(serializers.ModelSerializer):
    """ Logout Serializer"""
    class Meta:
        model = MyUser
        fields = []