from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response

from account.models import Followers
from posts.models import Posts
from .serializers import PostSerializer


class PostViewSets(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    """ Post ViewSet"""
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """ Get List of posts"""
        return Response({'status': status.HTTP_200_OK,
                         'message': 'List of users',
                         'data': PostSerializer(Posts.objects.filter(user=request.user), many=True).data},
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """Create post"""
        try:
            post = Posts.objects.create(user=request.user, title=request.POST.get('title'),
                                        description=request.POST.get('description'), image=request.FILES['image'])
            return Response({'status': status.HTTP_201_CREATED,
                             'message': 'Post created successfully',
                             'data': PostSerializer(post, many=False).data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FollowersPostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Follower Post ViewSet"""
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """get list of followers post"""
        following = Followers.objects.filter(follower=request.user).values('following')
        followers_post = Posts.objects.filter(user_id__in=following)
        return Response({'status': status.HTTP_200_OK,
                         'message': 'List of followers post',
                         'data': PostSerializer(followers_post, many=True).data},
                        status=status.HTTP_200_OK)
