from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import RegisterDriver


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

        db_exits_username = User.objects.get(username=username)
        if db_exits_username:
            messages.error(request, "This username already used")
            return call_pages(request, username, driver_phone_number, vehicle_type)

        db_exits_phone = RegisterDriver.objects.get(driver_phone_number=driver_phone_number)
        if db_exits_phone:
            messages.error(request, "This phone number already used")
            return call_pages(request, username, driver_phone_number, vehicle_type)

        if password != confirmPassword:
            messages.error(request, "Confirm password do not match.")
            return call_pages(request, username, driver_phone_number, vehicle_type)

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


def call_pages(request, username, driver_phone_number, vehicle_type):
    return render(request, 'Registration/driverRegistration.html', {
        'username': username,
        'driver_phone_number': driver_phone_number,
        'vehicle_type': vehicle_type,
    })

# Register Driver Views Code End


# Register Caretaker Views Code Start


# Register Caretaker Views Code End
