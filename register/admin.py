from django.contrib import admin
from .models import SocietyUser, RegisterDriver  # Import RegisterDriver here

# Register your models here.
admin.site.register(SocietyUser)
admin.site.register(RegisterDriver)
