# Generated by Django 4.2.7 on 2023-12-27 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0002_dayofweek_remove_trains_days_available_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trains',
            new_name='Train',
        ),
    ]
