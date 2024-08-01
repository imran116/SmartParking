# # forms.py
from django import forms
from .models import RegisterDriver
from django.contrib.auth.models import User
#
#
class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',]
#
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmPassword')
#         if password and confirm_password and password != confirm_password:
#           raise forms.ValidationError("Confirm Password do not match.")
#         return cleaned_data
#
#
class DriverRegisterProfileForm(forms.ModelForm):
     class Meta:
        model = RegisterDriver
        fields = ['driver_phone_number', 'vehicle_type', 'driver_profile_image', 'driver_license_image',
                  'driver_car_registration_image']
        widgets = {
            'vehicle_type': forms.RadioSelect(choices=RegisterDriver.VEHICLE_CHOICES)
         }

# register/forms.py
# from django import forms
# from .models import SocietyUser

# class SocietyUserRegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

#     class Meta:
#         model = SocietyUser
#         fields = ['username', 'phone', 'email', 'password', 'confirm_password', 'profile_picture', 'society_house_name', 'address']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
