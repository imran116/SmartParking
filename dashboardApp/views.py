from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from register.models import Socity, RegisterCaretaker
from addParkingApp.models import AddParkingSlot


# Create your views here.


# def dashboard_view(request):
#     return render(request, 'Dashboard/socityDashboard.html')

def socityDashboard_view(request):
    return render(request, 'Dashboard/socityDashboard.html')


def commercialDashboard_view(request):
    return render(request, 'Dashboard/commercialDashboard.html')


def ownerDashboard_view(request):
    return render(request, 'Dashboard/ownerDashboard.html')


def caretakerDashboard_view(request):
    return render(request, 'Dashboard/caretakerDashboard.html')


# Caretaker Space_Owner Dashboard Code Start

def caretaker_parking_map(request):
    if request.method == 'POST':
        mobile_no = request.POST.get("phone")
        print(mobile_no)  # for debug
        if Socity.objects.filter(society_phone=mobile_no).exists():
            society_obj = Socity.objects.get(society_phone=mobile_no)
            # society_user = Socity.objects.get(user=society_obj)
            parking_obj = AddParkingSlot.objects.filter(user=society_obj.user)
            register_caretaker = RegisterCaretaker.objects.get(user=request.user)
            register_caretaker.is_verify = True
            register_caretaker.save()
            return render(request, 'DashboardMenu/dashboardParkingMap_caretaker.html',
                          context={'parking_obj': parking_obj})
        else:
            messages.error(request, "not found.")
            print("not found")  # dor debug
    return render(request, 'varify_catetaker.html')


# Caretaker Space_Owner Dashboard Code End


def driverDashboard_view(request):
    return render(request, 'Dashboard/driverDashboard.html')


def dashboardAccount_view(request):
    return render(request, 'DashboardMenu/dashboardAccount.html')


def dashboardAddParkingSlot_view(request):
    return render(request, 'DashboardMenu/dashboardAddParkingSlot.html')


def dashboardAddSlotOwner_view(request):
    return render(request, 'DashboardMenu/dashboardAddSlotOwner.html')


def dashboardParkingMap_view(request):
    return render(request, 'DashboardMenu/dashboardParkingMap.html')


def dashboardBookFromParkingLot_view(request):
    return render(request, 'DashboardMenu/dashboardBookFromParkingLot.html')


def verify_caretaker(request):
    return render(request, 'varify_catetaker.html')
