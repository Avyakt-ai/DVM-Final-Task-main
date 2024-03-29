# Generated by Django 4.2.7 on 2024-01-02 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0009_remove_train_days_available_train_day_of_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='railway_staff.station'),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='railway_staff.station'),
        ),
    ]
