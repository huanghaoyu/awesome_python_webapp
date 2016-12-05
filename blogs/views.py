from django.shortcuts import render

from .models import Blog, User

def index(request):
    user = None
    if len(request.POST) != 0:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(name=name, email=email, password=password)
        user.save()
    blogs = Blog.objects.all()
    context = {
               'blogs': blogs,
               'user': user,
               }
    return render(request, 'blogs/blogs.html', context)

def register(request):
    return render(request, 'blogs/register.html')