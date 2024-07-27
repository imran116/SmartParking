from django.shortcuts import render, redirect
from .models import Driver
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        vehicle = request.POST['vehicle']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        profile_picture = request.FILES['profilePicture']
        driving_license = request.FILES['drivingLicence']
        car_registration = request.FILES['carRegistration']

        if password != confirm_password:
            return render(request, 'driver_registration.html', {'error': 'Passwords do not match'})

        fs = FileSystemStorage()
        profile_picture_name = fs.save(profile_picture.name, profile_picture)
        driving_license_name = fs.save(driving_license.name, driving_license)
        car_registration_name = fs.save(car_registration.name, car_registration)

        driver = Driver(
            username=username,
            phone=phone,
            vehicle=vehicle,
            password=password,
            profile_picture=profile_picture_name,
            driving_license=driving_license_name,
            car_registration=car_registration_name
        )
        driver.save()

        return redirect('home')

    return render(request, 'driver_registration.html')

