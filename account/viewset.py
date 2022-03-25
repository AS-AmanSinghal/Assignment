from django.contrib import auth
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from account.models import MyUser
from .serializer import MyUserSerializer, LoginSerializer, LogoutSerializer


class MyUserViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    """ User ViewSet"""
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def list(self, request, *args, **kwargs):
        """ Get the list of users """
        return Response({'status': status.HTTP_200_OK,
                         'message': 'List of users',
                         'data': MyUserSerializer(MyUser.objects.all(), many=True).data},
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """Create login user"""
        if request.POST.get('first_name') is None:
            return Response({'first_name': 'field required'})
        if request.POST.get('last_name') is None:
            return Response({'last_name': 'field required'})
        if request.POST.get('email') is None:
            return Response({'email': 'field required'})
        if request.POST.get('password') is None:
            return Response({'password': 'field required'})
        try:
            user = MyUser.objects.create_superuser(request.POST.get('first_name'), request.POST.get('last_name'),
                                                   request.POST.get('email'), request.POST.get('password'))
            return Response({'status': status.HTTP_201_CREATED,
                             'message': 'User created successfully',
                             'data': MyUserSerializer(user, many=False).data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """Login ViewSet"""
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """ For login user"""
        user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return Response({'status': status.HTTP_200_OK,
                                 'message': 'Login successfully',
                                 'data': LoginSerializer(user, many=False).data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                                 'error': 'Email/Password does not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'error': 'Email/Password does not match'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """ Logout ViewSet"""
    queryset = MyUser.objects.all()
    serializer_class = LogoutSerializer

    def create(self, request, *args, **kwargs):
        """ For logout user"""
        auth.logout(request)
        return Response({'status': status.HTTP_200_OK,
                         'message': 'Logout successfully.'}, status=status.HTTP_200_OK)
