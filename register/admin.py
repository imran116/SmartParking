from django.contrib import admin
from .models import Socity, RegisterDriver  # Import RegisterDriver here

# Register your models here.
# <<<<<<< HEAD
from django.contrib import admin
from .models import Socity,RegisterDriver,RegisterCaretaker,SpaceOwner

admin.site.register(Socity)
admin.site.register(SpaceOwner)

admin.site.register(RegisterDriver)
admin.site.register(RegisterCaretaker)
