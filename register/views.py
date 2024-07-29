from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import RegisterDriver, RegisterCaretaker,SpaceOwner


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

        db_exits_username = User.objects.filter(username=username)
        if db_exits_username:
            messages.error(request, "This username already used")
            return call_driver_pages(request, username, driver_phone_number, vehicle_type)

        db_exits_phone = RegisterDriver.objects.filter(driver_phone_number=driver_phone_number)
        if db_exits_phone:
            messages.error(request, "This phone number already used")
            return call_driver_pages(request, username, driver_phone_number, vehicle_type)

        if password != confirmPassword:
            messages.error(request, "Confirm password do not match.")
            return call_driver_pages(request, username, driver_phone_number, vehicle_type)

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


def call_driver_pages(request, username, driver_phone_number, vehicle_type):
    return render(request, 'Registration/driverRegistration.html', {
        'username': username,
        'driver_phone_number': driver_phone_number,
        'vehicle_type': vehicle_type,
    })


# Register Driver Views Code End

# Register Caretaker Views Code Start
def register_caretaker(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        caretaker_mobile_number = request.POST.get('caretaker_mobile_number')
        caretaker_profile_image = request.FILES.get('caretaker_profile_image')
        caretaker_nid_image = request.FILES.get('caretaker_nid_image')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        db_exists_username = User.objects.filter(username=username)
        if db_exists_username:
            messages.error(request, "This username already used.")
            return call_caretaker_pages(request, username, caretaker_mobile_number)

        db_exists_mobile = RegisterCaretaker.objects.filter(caretaker_mobile_number=caretaker_mobile_number)
        if db_exists_mobile:
            messages.error(request, "This mobile number already used")
            return call_caretaker_pages(request, username, caretaker_mobile_number)

        if password != confirmPassword:
            messages.error(request, "Confirm Password do not match")
            return call_caretaker_pages(request, username, caretaker_mobile_number)

        user = User.objects.create_user(username=username, password=password)

        RegisterCaretaker.objects.create(
            user=user,
            caretaker_mobile_number=caretaker_mobile_number,
            caretaker_profile_image=caretaker_profile_image,
            caretaker_nid_image=caretaker_nid_image

        )
        return redirect('caretakerDashboard')
    return render(request, 'Registration/caretakerRegistration.html')


def call_caretaker_pages(request, username, caretaker_mobile_number):
    return render(request, 'Registration/caretakerRegistration.html', {
        'username': username,
        'caretaker_mobile_number': caretaker_mobile_number
    })


# Register Caretaker Views Code End
#register space owner code starts


def spaceowner(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        owner_mobile_number = request.POST.get('owner_mobile_number')
        owner_email_address =request.POST.get('owner_email_address')
        owner_profile_image = request.FILES.get('owner_profile_image')
        owner_society_name= request.POST.get('owner_society_name')
        owner_address= request.POST.get('owner_address')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        db_exists_username = User.objects.filter(username=username)
        if db_exists_username:
            messages.error(request, "This username already used.")
            return call_owner_pages(request, username, owner_mobile_number)

        db_exists_mobile = SpaceOwner.objects.filter(owner_mobile_number=owner_mobile_number)
        if db_exists_mobile:
            messages.error(request, "This mobile number already used")
            return call_owner_pages(request, username, owner_mobile_number)

        if password != confirmPassword:
            messages.error(request, "Confirm Password do not match")
            return call_owner_pages(request, username, owner_mobile_number)

        user = User.objects.create_user(username=username, password=password)

        SpaceOwner.objects.create(
            user=user,
            owner_mobile_number=owner_mobile_number,
            owner_email_address=owner_email_address,
            owner_profile_image=owner_profile_image,
            owner_society_name=owner_society_name,
            owner_address= owner_address

        )
        return redirect('ownerDashboard')
    return render(request, 'Registration/ownerRegistration.html')


def call_owner_pages(request, username, owner_mobile_number):
    return render(request, 'Registration/ownerRegistration.html', {
        'username': username,
        'owner_mobile_number': owner_mobile_number
    })





#register space owner code ends

from django.shortcuts import render, redirect
from .forms import SocietyUserRegistrationForm


def societyRegistration_view(request):
    if request.method == 'POST':
        form = SocietyUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            user.save()

            print("User registered successfully: ", user)  # Debug print
            return redirect('socityDashboard')  # Adjust redirection as needed
        else:
            print("Form is not valid: ", form.errors)  # Debug print
    else:
        form = SocietyUserRegistrationForm()

    return render(request, 'Registration/socityRegistration.html', {'form': form})
