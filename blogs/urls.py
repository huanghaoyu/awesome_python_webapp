from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [
    # ex: /blogs/
    url(r'^$', views.index, name='index'),
    # ex: /blogs/register/
    url(r'^register/$', views.register, name='register'),
]
