from __future__ import unicode_literals

from django.db import models
import time

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField()
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/user_images/', max_length=204800)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Blog(models.Model):
    