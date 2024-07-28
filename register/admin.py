from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SocietyUser,RegisterDriver,RegisterCaretaker

admin.site.register(SocietyUser)


admin.site.register(RegisterDriver)
admin.site.register(RegisterCaretaker)