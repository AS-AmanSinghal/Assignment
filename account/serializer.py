from rest_framework import serializers

from account.models import MyUser, Followers


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


def get_user_name(id):
    user = MyUser.objects.get(id=id)
    return f'{user.first_name} {user.last_name}'


class FollowersSerializer(serializers.ModelSerializer):
    """ Followers Serializer"""
    follower = serializers.ReadOnlyField()

    class Meta:
        model = Followers
        fields = ['id', 'follower', 'following']

    def to_representation(self, instance):
        data = super(FollowersSerializer, self).to_representation(instance)
        data['follower'] = get_user_name(instance.follower.id)
        data['following'] = get_user_name(instance.following.id)
        return data
