# Generated by Django 4.2.7 on 2024-01-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0021_train_first_ac_fare_train_general_fare_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passengerinformation',
            name='age',
        ),
        migrations.AddField(
            model_name='passengerinformation',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]