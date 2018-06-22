
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'profile/<username>/',views.profile),
    url(r'profile/',views.profile)

    
]
