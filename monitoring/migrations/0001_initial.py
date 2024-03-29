# Generated by Django 4.0.5 on 2022-06-09 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name="Boat's Name")),
                ('owner', models.CharField(max_length=250, verbose_name="Owner's Name")),
                ('length', models.FloatField(help_text='(in meters)', verbose_name="Boat's Length")),
                ('width', models.FloatField(help_text='(in meters)', verbose_name="Boat's Width")),
                ('height', models.FloatField(help_text='(in meters)', verbose_name="Boat's Height")),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Registered at')),
            ],
            options={
                'ordering': ['-registered_at'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critical_pitch_angle', models.FloatField(help_text='(in degrees)', verbose_name='Critical Pitch Angle')),
                ('critical_roll_angle', models.FloatField(help_text='(in degrees)', verbose_name='Critical Roll Angle')),
                ('reading_rate', models.FloatField(help_text='(in milliseconds)', verbose_name='Reading Rate')),
                ('saving_rate', models.FloatField(help_text='(in milliseconds)', verbose_name='Saving Rate')),
                ('sms_rate', models.FloatField(help_text='(in milliseconds)', verbose_name='SMS Rate')),
                ('mobile_number', models.CharField(max_length=13, verbose_name='Mobile number for alarms')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_angle', models.FloatField(help_text='(in degrees)', verbose_name='Heading Angle')),
                ('pitch_angle', models.FloatField(help_text='(in degrees)', verbose_name='Pitch Angle')),
                ('roll_angle', models.FloatField(help_text='(in degrees)', verbose_name='Roll Angle')),
                ('gyro_x', models.FloatField(help_text='(in degrees per second)', verbose_name='Gyroscope-X (Yaw Rate)')),
                ('gyro_y', models.FloatField(help_text='(in degrees per second)', verbose_name='Gyroscope-Y (Roll Rate)')),
                ('gyro_z', models.FloatField(help_text='(in degrees per second)', verbose_name='Gyroscope-Z (Pitch Rate)')),
                ('accel_x', models.FloatField(help_text='(in meters per second)', verbose_name='Acceleration-X')),
                ('accel_y', models.FloatField(help_text='(in meters per second)', verbose_name='Acceleration-Y')),
                ('accel_z', models.FloatField(help_text='(in meters per second)', verbose_name='Acceleration-Z')),
                ('mag_x', models.FloatField(help_text='(in micro-Tesla)', verbose_name='Magnetometer-X')),
                ('mag_y', models.FloatField(help_text='(in micro-Tesla)', verbose_name='Magnetometer-Y')),
                ('mag_z', models.FloatField(help_text='(in micro-Tesla)', verbose_name='Magnetometer-Z')),
                ('latitude', models.FloatField(help_text='(in degrees)', verbose_name='Latitude')),
                ('longitude', models.FloatField(help_text='(in degrees)', verbose_name='Longitude')),
                ('altitude', models.FloatField(help_text='(in meters)', verbose_name='Altitude')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.boat', verbose_name='Boat')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
