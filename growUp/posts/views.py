from django.shortcuts import render
from .models import Posts

def get_posts(request):
    form = None
    if request.method == "POST":
        print("IN PROGRESS")
        return None
    posts_list = Posts.objects.all()
    return render(request, 'posts.html',{'posts':posts_list})

