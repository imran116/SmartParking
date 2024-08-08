from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', dashboard_view, name='dashboard'),
    path('socityDashboard/', socityDashboard_view, name='socityDashboard'),
    path('commercialDashboard/', commercialDashboard_view, name='commercialDashboard'),
    path('caretakerDashboard/', caretakerDashboard_view, name='caretakerDashboard'),
    path('ownerDashboard/', ownerDashboard_view, name='ownerDashboard'),
    path('add-parking/', space_owner_add_parking_view, name='space_owner_add_parking'),
    path('driverDashboard/', driverDashboard_view, name='driverDashboard'),
    path('dashboardAccount/', dashboardAccount_view, name='dashboardAccount'),
    path('dashboardAddParkingSlot/', dashboardAddParkingSlot_view, name='dashboardAddParkingSlot'),
    path('dashboardAddSlotOwner/', dashboardAddSlotOwner_view, name='dashboardAddSlotOwner'),
    path('dashboardParkingMap/', dashboardParkingMap_view, name='dashboardParkingMap'),
    path('dashboardBookFromParkingLot/', dashboardBookFromParkingLot_view, name='dashboardBookFromParkingLot'),

    path('verify-caretaker/', verify_caretaker, name='verify_caretaker'),
    path('verify-space-owner/', verify_space_owner, name='verify_space_owner'),
    path('/caretaker-parking-map/', caretaker_parking_map_verify, name='caretaker_map'),
    path('/space-owner-parking-map/', space_owner_parking_map_view, name='space_owner_map'),

]
