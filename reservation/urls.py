from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',welcometoapp),
    url(r'allhotels',showHotels),
    url(r'hotelsincity',showHotelsInCity),
    url(r'reservationlist',showReservationslist)
    
]