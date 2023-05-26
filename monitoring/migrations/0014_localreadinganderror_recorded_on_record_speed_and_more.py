# Generated by Django 4.0.5 on 2023-05-26 14:29

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0013_record_signalstrength_alter_bulletin_available_until_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='localreadinganderror',
            name='recorded_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='speed',
            field=models.FloatField(default=0, help_text='(in m/s)', verbose_name='Speed'),
        ),
        migrations.AddField(
            model_name='voyage',
            name='avg_speed',
            field=models.FloatField(default=0, verbose_name='Average Speed'),
        ),
        migrations.AddField(
            model_name='voyage',
            name='max_pitch',
            field=models.FloatField(default=0, verbose_name='Maximum Pitch'),
        ),
        migrations.AddField(
            model_name='voyage',
            name='max_roll',
            field=models.FloatField(default=0, verbose_name='Maximum Roll'),
        ),
        migrations.AddField(
            model_name='voyage',
            name='max_speed',
            field=models.FloatField(default=0, verbose_name='Maximum Speed'),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='available_until',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 26))], verbose_name='Available Until'),
        ),
        migrations.AlterField(
            model_name='record',
            name='voyage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.voyage', verbose_name='Voyage'),
        ),
    ]