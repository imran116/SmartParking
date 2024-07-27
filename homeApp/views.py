from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def home_view(request):
    return render(request, 'Index/index.html')

def login_view(request):
    return render(request, 'Login/login.html')

def caretakerRegistration_view(request):
    return render(request, 'Registration/caretakerRegistration.html')

def driverRegistration_view(request):
    return render(request, 'Registration/driverRegistration.html')

def ownerRegistration_view(request):
    return render(request, 'Registration/ownerRegistration.html')

def socityRegistration_view(request):
    return render(request, 'Registration/socityRegistration.html')

def availableParkingLots_view(request):
    return render(request, 'ParkingLot/availableParkingLots.html')

def bookFromParkingLot_view(request):
    return render(request, 'BookParking/bookFromParkingLot.html')

def otpVarification_view(request):
    return render(request, 'OTP/otpVarification.html')

def otpVarificationUnSuccessful_view(request):
    return render(request, 'OTP/otpVarificationUnSuccessful.html')