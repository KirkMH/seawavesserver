from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import date


class Boat(models.Model):
    name = models.CharField(
        _("Boat's Name"), 
        max_length=100,
        unique=True
    )
    owner = models.CharField(
        _("Owner's Name"), 
        max_length=250
    )
    owner_contact = models.CharField(
        _("Owner's Contact Number"), 
        max_length=50,
        null=True,
        blank=True,
        default=None
    )
    length = models.FloatField(
        _("Boat's Length"),
        help_text='(in meters)'
    )
    width = models.FloatField(
        _("Boat's Width"),
        help_text='(in meters)'
    )
    height = models.FloatField(
        _("Boat's Height"),
        help_text='(in meters)'
    )
    registered_at = models.DateTimeField(
        _("Registered at"), 
        auto_now=False, 
        auto_now_add=True
    )
    is_active = models.BooleanField(
        _("Is active?"),
        default=True
    )

    class Meta:
        ordering = ['-registered_at']

    def __str__(self):
        return self.name

    def last_location():
        last_record = self.record_set.last()
        return '%d, %d' % (last_record.latitude, last_record.longitude)
    

class Record(models.Model):
    boat = models.ForeignKey(
        Boat, 
        verbose_name=_("Boat"), 
        on_delete=models.CASCADE
    )
    heading_angle = models.FloatField(
        _("Heading Angle"),
        help_text='(in degrees)'
    )
    pitch_angle = models.FloatField(
        _("Pitch Angle"),
        help_text='(in degrees)'
    )
    roll_angle = models.FloatField(
        _("Roll Angle"),
        help_text='(in degrees)'
    )
    gyro_x = models.FloatField(
        _("Gyroscope-X (Yaw Rate)"),
        help_text='(in degrees per second)'
    )
    gyro_y = models.FloatField(
        _("Gyroscope-Y (Roll Rate)"),
        help_text='(in degrees per second)'
    )
    gyro_z = models.FloatField(
        _("Gyroscope-Z (Pitch Rate)"),
        help_text='(in degrees per second)'
    )
    accel_x = models.FloatField(
        _("Acceleration-X"),
        help_text='(in meters per second)'
    )
    accel_y = models.FloatField(
        _("Acceleration-Y"),
        help_text='(in meters per second)'
    )
    accel_z = models.FloatField(
        _("Acceleration-Z"),
        help_text='(in meters per second)'
    )
    mag_x = models.FloatField(
        _("Magnetometer-X"),
        help_text='(in micro-Tesla)'
    )
    mag_y = models.FloatField(
        _("Magnetometer-Y"),
        help_text='(in micro-Tesla)'
    )
    mag_z = models.FloatField(
        _("Magnetometer-Z"),
        help_text='(in micro-Tesla)'
    )
    latitude = models.FloatField(
        _("Latitude"),
        help_text='(in degrees)'
    )
    longitude = models.FloatField(
        _("Longitude"),
        help_text='(in degrees)'
    )
    altitude = models.FloatField(
        _("Altitude"),
        help_text='(in meters)'
    )
    timestamp = models.DateTimeField(
        _("Timestamp"), 
        auto_now=False, 
        auto_now_add=True
    )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '%s: %f° %f°' % (self.boat.name, self.latitude, self.longitude)

    def getColor(self):
        setting = Setting.objects.last()
        c_pitch = setting.critical_pitch_angle
        c_roll = setting.critical_roll_angle
        color = None
        if self.pitch_angle >= c_pitch or self.roll_angle >= c_roll:
            color = "red"
        elif self.pitch_angle >= (c_pitch * 0.9) or self.roll_angle >= (c_roll * 0.9):
            color = "orange"
        elif self.pitch_angle >= (c_pitch * 0.8) or self.roll_angle >= (c_roll * 0.8):
            color = "yellow"
        else:
            color = "black"
        return color


class Setting(models.Model):
    critical_pitch_angle = models.FloatField(
        _("Critical Pitch Angle"),
        help_text='(in degrees)'
    )
    critical_roll_angle = models.FloatField(
        _("Critical Roll Angle"),
        help_text='(in degrees)'
    )
    reading_rate = models.FloatField(
        _("Reading Rate"),
        help_text='(in milliseconds)'
    )
    saving_rate = models.FloatField(
        _("Saving Rate"),
        help_text='(in milliseconds)'
    )
    sms_rate = models.FloatField(
        _("SMS Rate"),
        help_text='(in milliseconds)'
    )
    post_rate = models.FloatField(
        _("Server Post Rate"),
        help_text='(in milliseconds)'
    )
    mobile_number = models.CharField(
        _("Mobile number for alarms"), 
        max_length=13
    )

    def __str__(self):
        return 'Setting #%d' % self.pk
    
    

class AvailableBulletin(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available_until__gte=date.today())


class Bulletin(models.Model):
    title = models.CharField(
        _("Title"), 
        max_length=250
    )
    message = models.TextField(_("Message"))
    available_until = models.DateField(
        _("Available Until"), 
        auto_now=False, 
        auto_now_add=False,
        validators=[MinValueValidator(date.today())]
    )
    created_at = models.DateTimeField(
        _("Created At"), 
        auto_now=False, 
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User, 
        verbose_name=_("Created By"), 
        on_delete=models.CASCADE
    )
    objects = models.Manager()
    available = AvailableBulletin()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    