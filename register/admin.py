from django.contrib import admin
from .models import SocietyUser, RegisterDriver  # Import RegisterDriver here

# Register your models here.
# <<<<<<< HEAD
from django.contrib import admin
from .models import SocietyUser,RegisterDriver,RegisterCaretaker

admin.site.register(SocietyUser)


admin.site.register(RegisterDriver)
admin.site.register(RegisterCaretaker)
