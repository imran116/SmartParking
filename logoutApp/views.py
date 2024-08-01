from django.contrib.auth import logout
from django.shortcuts import render


# Create your views here.

def logout_user(request):
    logout(request)
    return render(request, 'Index/index.html')