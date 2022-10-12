# Generated by Django 4.0.5 on 2022-10-12 08:26

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0009_alter_record_accel_x_alter_record_accel_y_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='registered_at',
            field=models.DateTimeField(verbose_name='Registered at'),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='available_until',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2022, 10, 12))], verbose_name='Available Until'),
        ),
    ]
