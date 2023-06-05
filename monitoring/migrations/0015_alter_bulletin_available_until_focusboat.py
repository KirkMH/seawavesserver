# Generated by Django 4.0.5 on 2023-06-05 14:01

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0014_localreadinganderror_recorded_on_record_speed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='available_until',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 6, 5))], verbose_name='Available Until'),
        ),
        migrations.CreateModel(
            name='FocusBoat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.boat')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
