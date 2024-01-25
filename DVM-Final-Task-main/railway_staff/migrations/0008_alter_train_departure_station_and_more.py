# Generated by Django 4.2.7 on 2023-12-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0007_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departure_station',
            field=models.CharField(choices=[(1, 'A'), (2, 'B')], max_length=100),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination_station',
            field=models.CharField(choices=[(1, 'A'), (2, 'B')], max_length=100),
        ),
    ]
