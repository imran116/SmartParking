from django.urls import path
from .views import *

app_name = 'loginApp'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('login-user/', user_login_view, name='society_login'),

]
