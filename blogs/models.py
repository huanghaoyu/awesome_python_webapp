from __future__ import unicode_literals

from django.db import models
import time

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField()
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogs/images/user_images')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    