# Generated by Django 5.0.7 on 2024-08-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addParkingApp', '0003_alter_addparkingslot_parking_slot_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addparkingslot',
            name='parking_slot_name',
            field=models.CharField(max_length=30),
        ),
    ]
