from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import RegisterDriver
from .forms import *


# Create your views here.

# Register Driver Views Code Start

def register_driver(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        driver_phone_number = request.POST.get('driver_phone_number')
        vehicle_type = request.POST.get('vehicle_type')
        driver_profile_image = request.FILES.get('driver_profile_image')
        driver_license_image = request.FILES.get('driver_license_image')
        driver_car_registration_image = request.FILES.get('driver_car_registration_image')

        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password != confirmPassword:
            messages.error(request, "Confirm password do not match.")
            return render(request, 'Registration/driverRegistration.html',{
                'username': username,
                'driver_phone_number': driver_phone_number,
                'vehicle_type':vehicle_type,
            })

        user = User.objects.create_user(username=username, password=password)

        RegisterDriver.objects.create(
            user=user,
            driver_phone_number=driver_phone_number,
            vehicle_type=vehicle_type,
            driver_profile_image=driver_profile_image,
            driver_license_image=driver_license_image,
            driver_car_registration_image=driver_car_registration_image
        )
        return redirect('driverDashboard')
    return render(request, 'Registration/driverRegistration.html')

# Register Driver Views Code End
