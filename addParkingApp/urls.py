from django.urls import path
from .views import add_parking_slot_views,parking_map_views, verify_society_view
app_name = 'addParkingApp'
urlpatterns = [
    path('/slot/', add_parking_slot_views, name='add_parking_slot'),
    path('/map/', parking_map_views, name='parking_map'),
    path('verify-society/', verify_society_view, name='verify_society'),

]