from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def home_view(request):
    return render(request, 'Index/index.html')

def login_view(request):
    return render(request, 'Login/login.html')