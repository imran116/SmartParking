from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


# def dashboard_view(request):
#     return render(request, 'Dashboard/socityDashboard.html')

def socityDashboard_view(request):
    return render(request, 'Dashboard/socityDashboard.html')

def commercialDashboard_view(request):
    return render(request, 'Dashboard/commercialDashboard.html')

def caretakerDashboard_view(request):
    return render(request, 'Dashboard/caretakerDashboard.html')

def ownerDashboard_view(request):
    return render(request, 'Dashboard/ownerDashboard.html')

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