# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel,Customer,Reservation

# from controllers.customer import *
# from controllers.hotel import *
# from controllers.main import *
# from controllers.notification import *
# from controllers.reservation import *


def welcometoapp(request):
    return HttpResponse('<h2>you are in the app</h2>')

def showHotels(request):
    allhotels="<ul>"
    for hotel in Hotel.objects.all():
        allhotels+="<li>"+hotel.hotel_name+"</li>"
    allhotels+="</ul>"
    return HttpResponse(allhotels)

def showHotelsInCity(request):
    lstcity=[]
    for hotel in Hotel.objects.all():
        if(hotel.hotel_city not in lstcity):
            lstcity.append(hotel.hotel_city)
    output=""
    for city in lstcity:
        output+="<h3> hotels in city of "+city+"</h3><ul>"
        for hc in Hotel.objects.all():
            if(hc.hotel_city==city):
                output+="<li>"+hc.hotel_name+"</li>"
        output+="</ul>"
    return HttpResponse(output)

def showReservationslist(request):
    output="<h2>Reservations : </h2><ul>"
    for res in Reservation.objects.all():
        output+="<li>"+res.__str__()+"</li>"
    output+="</ul>"
    return HttpResponse(output)




