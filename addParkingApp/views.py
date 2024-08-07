from django.contrib import messages
from django.shortcuts import render, redirect
from .models import AddParkingSlot
from register.models import Socity


# AddParkingSlot Views Code Start

def add_parking_slot_views(request):
    if request.method == 'POST':
        parking_slot_name = request.POST.get('parking_slot_name')
        parking_slot_owner_name = request.POST.get('parking_slot_owner_name')
        house_or_society_name = request.POST.get('house_or_society_name')
        parking_location = request.POST.get('parking_location')
        parking_address = request.POST.get('parking_address')
        parking_google_map_url = request.POST.get('parking_google_map_url')
        parking_charge_category = request.POST.get('parking_charge_category')
        parking_charge = request.POST.get('parking_charge')

        if AddParkingSlot.objects.filter(parking_slot_name=parking_slot_name, user=request.user).exists():
            messages.error(request, "This Parking Slot Name Already Used.")
            return redirect('dashboardAddParkingSlot')

        add_parking_obj = AddParkingSlot.objects.create(
            user=request.user,
            parking_slot_name=parking_slot_name,
            parking_slot_owner_name=parking_slot_owner_name,
            house_or_society_name=house_or_society_name,
            parking_location=parking_location,
            parking_address=parking_address,
            parking_google_map_url=parking_google_map_url,
            parking_charge_category=parking_charge_category,
            parking_charge=parking_charge
        )

        add_parking_obj.save()
        messages.success(request, "Parking Slot Added Successfully.")
        return redirect('dashboardAddParkingSlot')
    else:
        return render(request, 'DashboardMenu/dashboardAddParkingSlot.html')


# AddParkingSlot Views Code End

# ParkingMap Views Code Start

def parking_map_views(request):
    parking_obj = AddParkingSlot.objects.filter(user=request.user)
    parking_info = AddParkingSlot.objects.filter(user=request.user)[:1]
    society_owner = Socity.objects.filter(user=request.user)[0:1]
    return render(request, "DashboardMenu/dashboardParkingMap.html",
                  context={'parking_obj': parking_obj, 'parking_info': parking_info,'society_owner':society_owner})

# ParkingMap Views Code End


