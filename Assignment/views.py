from django.shortcuts import render, redirect


def home(request):
    """ For home page"""
    if request.user.is_authenticated:
        return render(request, 'auth/index.html')
    else:
        return redirect('login')
