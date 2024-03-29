# Generated by Django 4.2.7 on 2024-01-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0008_alter_train_departure_station_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='days_available',
        ),
        migrations.AddField(
            model_name='train',
            name='day_of_week',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=3),
        ),
        migrations.AlterField(
            model_name='train',
            name='departure_station',
            field=models.CharField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')], max_length=100),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination_station',
            field=models.CharField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')], max_length=100),
        ),
    ]
