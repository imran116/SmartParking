from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Register Driver Model Code Start

# Register Driver Model
class RegisterDriver(models.Model):
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('three_wheeler', 'Three Wheeler'),
        ('motorcycle', 'Motorcycle'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    driver_phone_number = models.CharField(max_length=20)
    driver_profile_image = models.ImageField(upload_to='driver_profile/')
    driver_license_image = models.ImageField(upload_to='driver_license/')
    driver_car_registration_image = models.ImageField(upload_to='driver_registration/')
    is_driver = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


# Register Driver Model Code  End


# Register Caretaker Model Code  Start
class RegisterCaretaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    caretaker_mobile_number = models.CharField(max_length=20)
    caretaker_profile_image = models.ImageField(upload_to='caretaker_profile/')
    caretaker_nid_image = models.ImageField(upload_to='caretaker_nid/')

    def __str__(self):
        return self.user.username


# Register Caretaker Model Code  End

# Register owner Model (starts)
class SpaceOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_mobile_number = models.CharField(max_length=20)
    owner_email_address = models.CharField(max_length=20)
    owner_profile_image = models.ImageField(upload_to='owner_profile/')
    owner_society_name = models.CharField(max_length=20)
    owner_address = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


# # Register owner Model (ends)
# >>>>>>> fd329138e9003b28395fa9c70c9cc692674b6195

# SocietyUser Model
class SocietyUserManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None):
        user = self.create_user(
            email,
            username=username,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SocietyUser(AbstractBaseUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    society_house_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last loginApp', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    objects = SocietyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

# User Type Model Code Start

# class UserType(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_mobile_number = models.CharField(max_length=20)
#     user_type = models.CharField(max_length=20)

# User Type Model Code End
