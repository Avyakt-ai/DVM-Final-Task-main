# Generated by Django 4.2.7 on 2024-01-05 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0016_alter_train_train_name_delete_trainnames'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
