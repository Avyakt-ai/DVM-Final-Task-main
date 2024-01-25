# Generated by Django 4.2.7 on 2024-01-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0024_remove_train_fare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departure_station',
            field=models.CharField(choices=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination_station',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]
