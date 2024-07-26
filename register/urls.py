# register/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('socityRegistration/', views.societyRegistration_view, name='society_registration'),
]
