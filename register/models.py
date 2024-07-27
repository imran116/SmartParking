from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Register Driver Model Code Start

class RegisterDriver(models.Model):
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('three_wheeler', 'Three Wheeler'),
        ('motorcycle', 'Motorcycle'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    driver_phone_number = models.CharField(max_length=20)
    driver_profile_image = models.ImageField(upload_to='driver_profile/')
    driver_license_image = models.ImageField(upload_to='driver_license/')
    driver_car_registration_image = models.ImageField(upload_to='driver_registration/')

    def __str__(self):
        return self.user.username

# Register Driver Model Code  End


# Register Caretaker Model Code  Start


# Register Caretaker Model Code  End
