from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from register.models import Socity,RegisterDriver,RegisterCaretaker, SpaceOwner


def login_view(request):
    return render(request, 'Login/login.html')


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('phone')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if RegisterDriver.objects.filter(user=request.user).exists():
                return redirect('driverDashboard')
            elif RegisterCaretaker.objects.filter(user=request.user).exists():
                return redirect('caretakerDashboard')
            elif Socity.objects.filter(user=request.user).exists():
                return redirect('socityDashboard')
            elif SpaceOwner.objects.filter(user=request.user).exists():
                return redirect('ownerDashboard')
            else:
                messages.error(request, "User not found.")
        else:
            messages.error(request, "Invalid email or password.")

        return render(request, 'Login/login.html')

    return render(request, 'Login/login.html')
