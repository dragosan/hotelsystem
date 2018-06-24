from django.http import HttpResponse

# code not used now after making new app reservation and add database to it


""" from controllers.customer import *
from controllers.hotel import *
from controllers.main import *
from controllers.notification import *
from controllers.reservation import * """


def welcome(request):
    return HttpResponse('<h2>welcome to our system</h2>')


"""def helloworld(request):
    return HttpResponse('hello mostafa')


#def content():
    # contents=hotellist()
    # return contents

def hotellist(request):
    hotels = Hotel.list_hotels()

    hotelsoutput = welcome()+"<br><ul>"
    for h in hotels:
        hotelsoutput += "<li>"+h.hotel_name+"</li>"
    hotelsoutput += "</ul>"
    hotelsoutput += "<br>"
    hotelsoutput += "choose city : "
    hotelsoutput += "<select name='selectCity'>"
    lst = []
    for h in hotels:

        if(h.city not in lst):
            lst.append(h.city)
    for ls in lst:
        hotelsoutput += "<option>"+ls+"</option>"
    hotelsoutput += "</option>"
    # hotelsoutput+=reservationsList()

    # return hotelsoutput
    return HttpResponse(hotelsoutput)


def list_hotels_by_city(request):
    all_cities = Hotel.hotels_in_city
    lst = []

    for item in all_cities:
        if(item[1] not in lst):
            lst.append(item[1])
    details = '<h3> List hotels by city  </h3>'
    # count=0
    for city in lst:

        details += "<h3> city name : "+city+"</h3><ol type='I'>"
        for h in all_cities:

            if(h[1] == city):

                details += "<li>"+h[0]+"</li>"
                # count=count+1
        details += "</ol>"
    return HttpResponse(details)


def list_hotels_in_city(request, city):
    hotels_in_city = Hotel.list_hotels_in_city(city)
    output = "<ul>"
    for h in hotels_in_city:
        output += "<li>"+h[0]+"</li>"
    output += "</ul>"
    return HttpResponse(city)


def reservationsList(request):
    resList = Reservation.returnList()
    resListoutput = "<br><ol>"
    for res in resList:
        resListoutput += "<li> reservation by customer name " + \
            (res[0].customer_name).capitalize() + \
            " for hotel "+res[1].hotel_name+"</li>"

    resListoutput += "</ol>"
    return HttpResponse(resListoutput)


def index(request):
    return HttpResponse(hotellist) """
