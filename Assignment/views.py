from django.shortcuts import render, redirect

from account.models import Followers, MyUser


def home(request):
    """ For home page"""
    if request.user.is_authenticated:
        following = Followers.objects.filter(follower=request.user).values('following')
        print(following)
        user_not_follow = MyUser.objects.exclude(id__in=following).exclude(id=request.user.id)
        context = {
            'user_not_follow': user_not_follow
        }
        return render(request, 'auth/index.html', context=context)
    else:
        return redirect('login')
