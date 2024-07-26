# register/views.py
from django.shortcuts import render, redirect
from .forms import SocietyUserRegistrationForm

def societyRegistration_view(request):
    if request.method == 'POST':
        form = SocietyUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("User registered successfully: ", user)  # Debug print
            return redirect('socityDashboard')  # Adjust redirection as needed
        else:
            print("Form is not valid: ", form.errors)  # Debug print
    else:
        form = SocietyUserRegistrationForm()

    return render(request, 'Registration/socityRegistration.html', {'form': form})


