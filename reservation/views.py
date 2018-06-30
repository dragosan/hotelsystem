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
    #return HttpResponse('<h2>you are in the app</h2>')
    return render(request,"reservation/welcome.html")

def showHotels(request):
    return render(request,"reservation/hotels.html",
              {'allhotels':Hotel.objects.all()})



    """ allhotels="<ul>"
    for hotel in Hotel.objects.all():
        allhotels+="<li>"+hotel.hotel_name+"</li>"
    allhotels+="</ul>"
    return HttpResponse(allhotels) """

def showHotelsInCity(request):

    
    lstcity=[]
    for hotel in Hotel.objects.all():
        if(hotel.hotel_city not in lstcity):
            lstcity.append(hotel.hotel_city)
    output=""
    lsthotelscity=[]
    lst=[]
    for city in lstcity:
                      
        for hc in Hotel.objects.all():
            
            if(hc.hotel_city==city):
                lst.append(hc)
            lsthotelscity.append(lst)        
        
    
    return render(request,'reservation/hotelsincity.html',{'lstcity':lstcity,'hotels':Hotel.objects.all()})

def showReservationslist(request):
    return render(request,"reservation/reservation.html",{'reservations':Reservation.objects.all()})




