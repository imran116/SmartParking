# register/forms.py
from django import forms
from .models import SocietyUser

class SocietyUserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = SocietyUser
        fields = ['username', 'phone', 'email', 'password', 'confirm_password', 'profile_picture', 'society_house_name', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
