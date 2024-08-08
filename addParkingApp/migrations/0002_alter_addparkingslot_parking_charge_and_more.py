# Generated by Django 5.0.7 on 2024-08-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addParkingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addparkingslot',
            name='parking_charge',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='addparkingslot',
            name='parking_charge_category',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('monthly', 'Monthly')], max_length=20),
        ),
    ]