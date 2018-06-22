# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request,username='default user'):
    return HttpResponse('<h1>welcome to my personal page : {}.</h1>'.format(username))

def profile(request):
    return HttpResponse('<h1>welcome to my personal page : {}.</h1>')