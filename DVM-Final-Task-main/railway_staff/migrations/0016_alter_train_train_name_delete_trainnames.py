# Generated by Django 4.2.7 on 2024-01-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway_staff', '0015_trainschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='train_name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='TrainNames',
        ),
    ]
