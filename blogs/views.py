from django.shortcuts import render

from .models import Blog, User

def index(request):
    blogs = Blog.objects.all()
    user = User.objects.all()[0]
    context = {
               'blogs': blogs,
               'user': user,
               }
    return render(request, 'blogs/blogs.html', context)
