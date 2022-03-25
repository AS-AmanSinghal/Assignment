from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response

from posts.models import Posts
from .serializers import PostSerializer


class AddPostViewSets(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response({'status': status.HTTP_200_OK,
                         'message': 'List of users',
                         'data': PostSerializer(Posts.objects.filter(user=request.user), many=True).data},
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
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
