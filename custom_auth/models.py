from django.db import models
from django.contrib.auth.hashers import make_password

class Driver(models.Model):
    username = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    vehicle = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    driving_license = models.ImageField(upload_to='driving_licenses/')
    car_registration = models.ImageField(upload_to='car_registrations/')
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
