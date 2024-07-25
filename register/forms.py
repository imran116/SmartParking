# # forms.py
# from django import forms
# from .models import RegisterDriver
# from django.contrib.auth.models import User
#
#
# class DriverRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username',]
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirmPassword')
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Confirm Password do not match.")
#         return cleaned_data
#
#
# class DriverRegisterProfileForm(forms.ModelForm):
#     class Meta:
#         model = RegisterDriver
#         fields = ['driver_phone_number', 'vehicle_type', 'driver_profile_image', 'driver_license_image',
#                   'driver_car_registration_image']
#         widgets = {
#             'vehicle_type': forms.RadioSelect(choices=RegisterDriver.VEHICLE_CHOICES)
#         }
