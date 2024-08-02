
from django.urls import path
from .views import *
from . import views 
app_name = 'register'
urlpatterns = [
    path('driver-registration/', register_driver, name='driver-registration'),
    path('caretaker-registration/', register_caretaker, name='caretaker-registration'),
    path('socityRegistration/', societyRegistration, name='society_registration'),
    path('owner-registration/', spaceowner, name='owner-registration'),
    
]
