from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def logout_user(request):
    logout(request)
    return render(request, 'Index/index.html')
