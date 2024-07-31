from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('loginApp/', login_view, name='loginApp'),
    path('caretakerRegistration/', caretakerRegistration_view, name='caretakerRegistration'),
    path('driverRegistration/', driverRegistration_view, name='driverRegistration'),    
    path('ownerRegistration/', ownerRegistration_view, name='ownerRegistration'),    
    path('socityRegistration/', socityRegistration_view, name='socityRegistration'),
    path('availableParkingLots/', availableParkingLots_view, name='availableParkingLots'),
    path('bookFromParkingLot/', bookFromParkingLot_view, name='bookFromParkingLot'),
    path('otpVarification/', otpVarification_view, name='otpVarification'),
    path('otpVarificationUnSuccessful/', otpVarificationUnSuccessful_view, name='otpVarificationUnSuccessful'),
]
