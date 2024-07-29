from django.contrib import admin
from .models import SocietyUser, RegisterDriver  # Import RegisterDriver here

# Register your models here.
# <<<<<<< HEAD
from django.contrib import admin
from .models import SocietyUser,RegisterDriver,RegisterCaretaker,SpaceOwner

admin.site.register(SocietyUser)
admin.site.register(SpaceOwner)

admin.site.register(RegisterDriver)
admin.site.register(RegisterCaretaker)
