# Generated by Django 5.0.2 on 2024-07-16 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('vehicle', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('driving_license', models.ImageField(upload_to='driving_licenses/')),
                ('car_registration', models.ImageField(upload_to='car_registrations/')),
            ],
        ),
    ]
