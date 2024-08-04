from django.urls import path
from .views import add_parking_slot_views
app_name = 'addParkingApp'
urlpatterns = [
    path('slot', add_parking_slot_views, name='add_parking_slot')

]