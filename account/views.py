from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from account.models import MyUser


# Create your views here.


def registration(request):
    if request.method == 'POST':
        user = MyUser.objects.create_superuser(first_name=request.POST.get('first_name'),
                                               last_name=request.POST.get('last_name'),
                                               email=request.POST.get('email'),
                                               password=request.POST.get('password'))
        auth.login(request, user)
        return HttpResponse(user)
    return render(request, 'auth/register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponse("Login")
        else:
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html')


@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')