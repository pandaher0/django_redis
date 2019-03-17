# Author:hxj
from django.urls import re_path
from booktest import views

urlpatterns = [
    re_path('^set_session$', views.set_session),
    re_path('^get_session$', views.get_session),
]
