from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from posts.models import Posts


@login_required(login_url='login')
def add_post(request):
    """ For create post """
    if request.method == 'POST':
        try:
            Posts.objects.create(user=request.user, title=request.POST.get('title'),
                                 description=request.POST.get('description'), image=request.FILES['image'])
            messages.success(request, 'Post created successfully.')
            return redirect('home')
        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'post/add.html')
    else:
        return render(request, 'post/add.html')