# Generated by Django 4.2.7 on 2024-01-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0031_alter_train_departure_station_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departure_station',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=100),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination_station',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=100),
        ),
    ]
