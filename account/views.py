from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from account.models import MyUser


# Create your views here.


def registration(request):
    if request.method == 'POST':
        try:
            user = MyUser.objects.create_superuser(first_name=request.POST.get('first_name'),
                                                   last_name=request.POST.get('last_name'),
                                                   email=request.POST.get('email'),
                                                   password=request.POST.get('password'))
            auth.login(request, user)
            messages.success(request, 'Register Successfully')
            return redirect('home')
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'auth/register.html')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Login Successfully')
                    return redirect('home')
            else:
                messages.error(request, 'Email/Password not match')
                return render(request, 'auth/login.html')
        else:
            return render(request, 'auth/login.html')
    else:
        return redirect('home')


@login_required(login_url='login')
def user_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logout successfully.')
        return redirect('login')
