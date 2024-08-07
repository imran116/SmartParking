from django.urls import path
from .views import add_parking_slot_views,parking_map_views
app_name = 'addParkingApp'
urlpatterns = [
    path('slot/', add_parking_slot_views, name='add_parking_slot'),
    path('map/', parking_map_views, name='parking_map'),

]