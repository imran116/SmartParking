from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', dashboard_view, name='dashboard'),
    path('socityDashboard/', socityDashboard_view, name='socityDashboard'),
    path('commercialDashboard/', commercialDashboard_view, name='commercialDashboard'),
    path('caretakerDashboard/', caretakerDashboard_view, name='caretakerDashboard'),
    path('ownerDashboard/', ownerDashboard_view, name='ownerDashboard'),
    path('driverDashboard/', driverDashboard_view, name='driverDashboard'),
    path('dashboardAccount/', dashboardAccount_view, name='dashboardAccount'),
    path('dashboardAddParkingSlot/', dashboardAddParkingSlot_view, name='dashboardAddParkingSlot'),
    path('dashboardAddSlotOwner/', dashboardAddSlotOwner_view, name='dashboardAddSlotOwner'),
    path('dashboardParkingMap/', dashboardParkingMap_view, name='dashboardParkingMap'),
    path('dashboardBookFromParkingLot/', dashboardBookFromParkingLot_view, name='dashboardBookFromParkingLot'),


]
