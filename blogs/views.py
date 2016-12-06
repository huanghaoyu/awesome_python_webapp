# -*- coding: utf-8 -*-

import sys, os
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(PROJ_DIR, 'awesome_python_webapp'))

import datetime, hashlib
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Blog, User
from settings import SECRET_KEY

def index(request):
    user = None
    signed_cookie = None
    if request.method == 'POST':
        name = request.POST.get('name', 'Unknown')
        email = request.POST.get('email', 'Unknown')
        password = request.POST.get('password', 'Unknown')
        if 'from_page' in request.COOKIES:
            if request.COOKIES['from_page'] == 'register':
                user = User(name=name, email=email, password=password)
                user.save()
            elif request.COOKIES['from_page'] == 'signin':
                try:
                    user = get_object_or_404(User, email=email)
                except Http404:
                    return render(request, reverse('blogs/register'))
                if user.password != password:
                    return render(request, reverse('blogs/signin'))
            else:
                pass
            signed_cookie = make_signed_cookie(str(user.id), user.password)
    if 'signed_cookie' in request.COOKIES:
        id = request.COOKIES['signed_cookie'].split('-')[0]
        try:
            user = get_object_or_404(User, pk=id)
        except Http404:
            pass
        if not verify_signed_cookie(request.COOKIES['signed_cookie'], user.password):
            print 'Not login'
            user = None
    blogs = Blog.objects.all()
    context = {
               'blogs': blogs,
               'user': user,
               }
    response = render(request, 'blogs/index.html', context)
    if signed_cookie is not None:
        response.set_cookie('signed_cookie', signed_cookie)
    return response

def register(request):
    response = render(request, 'blogs/register.html')
    response.set_cookie('from_page', 'register')
    return response

def signin(request):
    response = render(request, 'blogs/signin.html')
    response.set_cookie('from_page', 'signin')
    return response



def verify_signed_cookie(signed_cookie, password):
    '''
        验证登录cookie
    '''
    id, md5_code = signed_cookie.split('-')
    return signed_cookie == make_signed_cookie(id, password)

def make_signed_cookie(id, password):
    '''
        计算登录cookie
    '''
    L = [id, hashlib.md5('%s%s%s' % (id, password, SECRET_KEY)).hexdigest()]
    return '-'.join(L)


