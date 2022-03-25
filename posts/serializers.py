from rest_framework import serializers

from posts.models import Posts


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Posts
        fields = ['id', 'image', 'title', 'description']
