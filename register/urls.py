
from django.urls import path
from .views import *
app_name = 'register'
urlpatterns = [
    path('driver-registration/', register_driver, name='driver-registration'),
    path('socityRegistration/', views.societyRegistration_view, name='society_registration'),

]
