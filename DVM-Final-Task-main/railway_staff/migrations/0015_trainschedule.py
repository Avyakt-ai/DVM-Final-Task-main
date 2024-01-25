# Generated by Django 4.2.7 on 2024-01-04 06:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0014_train_reaching_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField(default=django.utils.timezone.now)),
                ('arrival_date', models.DateField(default=django.utils.timezone.now)),
                ('available_seats', models.IntegerField(default=0)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='railway_staff.train')),
            ],
        ),
    ]
