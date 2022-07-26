# Generated by Django 4.0.5 on 2022-07-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0008_alter_record_altitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='accel_x',
            field=models.FloatField(help_text='(in meters per second)', verbose_name='Acceleration-X'),
        ),
        migrations.AlterField(
            model_name='record',
            name='accel_y',
            field=models.FloatField(help_text='(in meters per second)', verbose_name='Acceleration-Y'),
        ),
        migrations.AlterField(
            model_name='record',
            name='accel_z',
            field=models.FloatField(help_text='(in meters per second)', verbose_name='Acceleration-Z'),
        ),
        migrations.AlterField(
            model_name='record',
            name='altitude',
            field=models.FloatField(default=0, help_text='(in meters)', verbose_name='Altitude'),
        ),
        migrations.AlterField(
            model_name='record',
            name='gyro_x',
            field=models.FloatField(help_text='(in degrees per second)', verbose_name='Gyroscope-X (Yaw Rate)'),
        ),
        migrations.AlterField(
            model_name='record',
            name='gyro_y',
            field=models.FloatField(help_text='(in degrees per second)', verbose_name='Gyroscope-Y (Roll Rate)'),
        ),
        migrations.AlterField(
            model_name='record',
            name='gyro_z',
            field=models.FloatField(help_text='(in degrees per second)', verbose_name='Gyroscope-Z (Pitch Rate)'),
        ),
        migrations.AlterField(
            model_name='record',
            name='heading_angle',
            field=models.FloatField(help_text='(in degrees)', verbose_name='Heading Angle'),
        ),
        migrations.AlterField(
            model_name='record',
            name='latitude',
            field=models.FloatField(help_text='(in degrees)', verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='record',
            name='longitude',
            field=models.FloatField(help_text='(in degrees)', verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='record',
            name='mag_x',
            field=models.FloatField(help_text='(in micro-Tesla)', verbose_name='Magnetometer-X'),
        ),
        migrations.AlterField(
            model_name='record',
            name='mag_y',
            field=models.FloatField(help_text='(in micro-Tesla)', verbose_name='Magnetometer-Y'),
        ),
        migrations.AlterField(
            model_name='record',
            name='mag_z',
            field=models.FloatField(help_text='(in micro-Tesla)', verbose_name='Magnetometer-Z'),
        ),
        migrations.AlterField(
            model_name='record',
            name='pitch_angle',
            field=models.FloatField(help_text='(in degrees)', verbose_name='Pitch Angle'),
        ),
        migrations.AlterField(
            model_name='record',
            name='roll_angle',
            field=models.FloatField(help_text='(in degrees)', verbose_name='Roll Angle'),
        ),
    ]