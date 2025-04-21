from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import EmailAuthenticationForm
from django.contrib.auth.models import User
from posts.models import Posts

def user_login(request):
    form = None
    if request.method == "POST":
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            user = form.get_user()
            print(user.first_name)
            posts = Posts.objects.all().order_by('-created_at')
            return render(request, 'home.html', {'user_profile': user, 'posts': posts})

        else:
            form = EmailAuthenticationForm()
    return render(request, 'login.html',{'form':form})
    