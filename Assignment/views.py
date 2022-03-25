from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from account.models import Followers, MyUser
from posts.models import Posts


def get_user_not_follow_data(request):
    """User not follow data"""
    following = Followers.objects.filter(follower=request.user).values('following')
    user_not_follow = MyUser.objects.exclude(id__in=following).exclude(id=request.user.id)
    return user_not_follow


def get_followers_post_data(request):
    """User not follow data"""
    following = Followers.objects.filter(follower=request.user).values('following')
    followers_post = Posts.objects.filter(user_id__in=following)
    paginator = Paginator(followers_post, 10)
    page_number = request.GET.get('follower_post_page')
    followers_post_page_obj = paginator.get_page(page_number)
    return followers_post_page_obj


def get_my_post_data(request):
    """My post data"""
    my_posts = Posts.objects.filter(user=request.user)
    paginator = Paginator(my_posts, 10)
    page_number = request.GET.get('page')
    my_post_page_obj = paginator.get_page(page_number)
    return my_post_page_obj


def home(request):
    """ For home page"""
    if request.user.is_authenticated:
        user_not_follow_page_obj = get_user_not_follow_data(request)
        my_post_page_obj = get_my_post_data(request)
        followers_post_page_obj = get_followers_post_data(request)
        context = {
            'my_post_page_obj': my_post_page_obj,
            'user_not_follow_page_obj': user_not_follow_page_obj,
            'followers_post_page_obj': followers_post_page_obj
        }
        return render(request, 'auth/index.html', context=context)
    else:
        return redirect('login')
