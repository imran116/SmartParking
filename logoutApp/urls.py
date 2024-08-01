from django.urls import path
from .views import logout_user
app_name = 'logoutApp'
urlpatterns = [
    path('user', logout_user, name='logout_user')

]
