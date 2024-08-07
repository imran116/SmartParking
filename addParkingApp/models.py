from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# AddParkingSlot Model Code Start

class AddParkingSlot(models.Model):
    PARKING_CHARGE_CATEGORY = [
        ('hourly', 'Hourly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_slot_name = models.CharField(max_length=30)
    parking_slot_owner_name = models.CharField(max_length=30)
    house_or_society_name = models.CharField(max_length=30)
    parking_location = models.CharField(max_length=30)
    parking_address = models.CharField(max_length=50)
    parking_google_map_url = models.URLField(max_length=500)
    parking_charge_category = models.CharField(max_length=20, choices=PARKING_CHARGE_CATEGORY)
    parking_charge = models.IntegerField(default=0)

    is_vacant = models.BooleanField(default=True)
    is_occupied = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_engaged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.parking_slot_owner_name} -- {self.parking_slot_name}"

# AddParkingSlot Model Code End
