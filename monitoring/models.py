from django.db import models
from django.db.models import Max, Avg
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from datetime import date


class Adopter(models.Model):
    code = models.CharField(
        _("Adopter Code"), 
        max_length=6,
        unique=True
    )
    name = models.CharField(
        _("Adopter's Name"), 
        max_length=100
    )
    address = models.CharField(
        _("Adopter's Address"), 
        max_length=250
    )
    contact_person = models.CharField(
        _("Adopter's Contact Person"), 
        max_length=100
    )
    email = models.EmailField(
        _("Adopter's Email"),
        max_length=250
    )
    phone = models.CharField(
        _("Adopter's Phone"),
        max_length=50,
        null=True,
        blank=True,
        default=None
    )
    map_title = models.CharField(
        _("Map Title"),
        max_length=100,
        default="Map"
    )
    map_center_lat = models.FloatField(
        _("Map Center Latitude"),
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        default=0
    )
    map_center_lng = models.FloatField(
        _("Map Center Longitude"),
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        default=0
    )
    map_zoom = models.IntegerField(
        _("Map Zoom"),
        default=12
    )
    
    def __str__(self):
        return self.name


class Boat(models.Model):
    adopter = models.ForeignKey(
        Adopter, 
        verbose_name=_("Adopter"), 
        null=True,
        blank=True,
        default=None,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        _("Boat's Name"), 
        max_length=100
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
        help_text='(in meters)',
        validators=[MinValueValidator(0)]
    )
    width = models.FloatField(
        _("Boat's Width"),
        help_text='(in meters)',
        validators=[MinValueValidator(0)]
    )
    height = models.FloatField(
        _("Boat's Height"),
        help_text='(in meters)',
        validators=[MinValueValidator(0)]
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
        unique_together = ('name', 'owner', 'adopter')

    def __str__(self):
        return self.name
    
    @property
    def is_still_navigating(self):
        voyage = Voyage.objects.filter(boat=self).last()
        print(f"Voyage: {voyage}")
        if voyage:
            return voyage.get_ended_at() == None
        else:
            return False

    def last_location(self):
        last_record = self.record_set.last()
        return '%d, %d' % (last_record.latitude, last_record.longitude)
    
    def get_color(self):
        rec = Record.objects.filter(boat=self).last()
        if rec:
            return rec.getColor()
        else:
            return 'blue'
        

class Voyage(models.Model):
    boat = models.ForeignKey(
        Boat, 
        verbose_name=_("Boat"), 
        on_delete=models.CASCADE
    )
    started_at = models.DateTimeField(
        _("Started At"), 
        auto_now=False, 
        auto_now_add=True
    )
    ended_at = models.DateTimeField(
        _("Ended At"), 
        auto_now=False, 
        auto_now_add=False,
        null=True, blank=True, default=None
    )
    max_roll = models.FloatField(_("Maximum Roll"), default=0)
    max_pitch = models.FloatField(_("Maximum Pitch"), default=0)
    max_speed = models.FloatField(_("Maximum Speed"), default=0)
    avg_speed = models.FloatField(_("Average Speed"), default=0)
    

    def calculate_fields(self):
        records = Record.objects.filter(voyage=self)
        roll = 0
        pitch = 0
        for r in records:
            if abs(r.roll_angle) > roll: roll = r.roll_angle
            if abs(r.pitch_angle) > pitch: pitch = r.pitch_angle

        self.max_roll = roll
        self.max_pitch = pitch
        self.max_speed = records.aggregate(max=Max('speed'))['max']
        self.avg_speed = records.aggregate(avg=Avg('speed'))['avg']
        self.save()

    def get_ended_at(self):
        return self.ended_at if self.ended_at else None

    def __str__(self):
        ended = self.ended_at.strftime("%m/%d/%y %H:%M:%S") if self.ended_at else 'ongoing'
        return f'{self.boat.name} ({self.started_at.strftime("%m/%d/%y %H:%M:%S")} - {ended})'
    

class Record(models.Model):
    boat = models.ForeignKey(
        Boat, 
        verbose_name=_("Boat"), 
        on_delete=models.CASCADE
    )
    voyage = models.ForeignKey(
        Voyage, 
        verbose_name=_("Voyage"), 
        on_delete=models.CASCADE,
        null=True, blank=True, default=None
    )
    heading_angle = models.FloatField(
        _("Heading Angle"),
        help_text='(in degrees)',
    )
    pitch_angle = models.FloatField(
        _("Pitch Angle"),
        help_text='(in degrees)',
    )
    roll_angle = models.FloatField(
        _("Roll Angle"),
        help_text='(in degrees)',
    )
    gyro_x = models.FloatField(
        _("Gyroscope-X (Yaw Rate)"),
        help_text='(in degrees per second)',
    )
    gyro_y = models.FloatField(
        _("Gyroscope-Y (Roll Rate)"),
        help_text='(in degrees per second)',
    )
    gyro_z = models.FloatField(
        _("Gyroscope-Z (Pitch Rate)"),
        help_text='(in degrees per second)',
    )
    accel_x = models.FloatField(
        _("Acceleration-X"),
        help_text='(in meters per second)',
    )
    accel_y = models.FloatField(
        _("Acceleration-Y"),
        help_text='(in meters per second)',
    )
    accel_z = models.FloatField(
        _("Acceleration-Z"),
        help_text='(in meters per second)',
    )
    mag_x = models.FloatField(
        _("Magnetometer-X"),
        help_text='(in micro-Tesla)',
    )
    mag_y = models.FloatField(
        _("Magnetometer-Y"),
        help_text='(in micro-Tesla)',
    )
    mag_z = models.FloatField(
        _("Magnetometer-Z"),
        help_text='(in micro-Tesla)',
    )
    latitude = models.FloatField(
        _("Latitude"),
        help_text='(in degrees)',
    )
    longitude = models.FloatField(
        _("Longitude"),
        help_text='(in degrees)',
    )
    altitude = models.FloatField(
        _("Altitude"),
        help_text='(in meters)',
        default=0
    )
    signalStrength = models.PositiveSmallIntegerField()
    speed = models.FloatField(
        _("Speed"),
        help_text='(in m/s)',
        default=0
    )
    timestamp = models.DateTimeField(
        _("Time Received"), 
        auto_now=False, 
        auto_now_add=True
    )
    sent_timestamp = models.CharField(
        _("Time Sent"), 
        max_length=25
    )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '%s: %f° %f°' % (self.boat.name, self.latitude, self.longitude)

    def getColor(self):
        setting = Setting.objects.last()
        color = "blue"
        if setting:
            c_pitch = setting.critical_pitch_angle
            c_roll = setting.critical_roll_angle
            pitch_angle = abs(self.pitch_angle)
            roll_angle = abs(self.roll_angle)
            if pitch_angle >= c_pitch or roll_angle >= c_roll:
                color = "red"
            elif pitch_angle >= (c_pitch * 0.9) or roll_angle >= (c_roll * 0.9):
                color = "orange"
            elif pitch_angle >= (c_pitch * 0.8) or roll_angle >= (c_roll * 0.8):
                color = "yellow"
        return color
    

class LocalReadingAndError(models.Model):
    boat = models.ForeignKey(
        Boat, 
        verbose_name=_("Boat"), 
        on_delete=models.CASCADE
    )
    readings = models.TextField()
    errors = models.TextField(null=True, blank=True, default=None)
    recorded_on = models.DateField(auto_now=False, auto_now_add=True)
    


class Setting(models.Model):
    adopter = models.OneToOneField(
        Adopter, 
        verbose_name=_("Adopter"), 
        null=True,
        blank=True,
        default=None,
        on_delete=models.CASCADE,
    )
    critical_pitch_angle = models.FloatField(
        _("Critical Pitch Angle"),
        help_text='(in degrees)',
        default=15.0
    )
    critical_roll_angle = models.FloatField(
        _("Critical Roll Angle"),
        help_text='(in degrees)',
        default=20.0
    )
    reading_rate = models.FloatField(
        _("Reading Rate"),
        help_text='(in milliseconds)',
        default=250.0
    )
    saving_rate = models.FloatField(
        _("Saving Rate"),
        help_text='(in milliseconds)',
        default=60000.0
    )
    sms_rate = models.FloatField(
        _("SMS Rate"),
        help_text='(in milliseconds)',
        default=60000.0
    )
    post_rate = models.FloatField(
        _("Server Post Rate"),
        help_text='(in milliseconds)',
        default=60000.0
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
    adopter = models.ForeignKey(
        Adopter, 
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Adopter"), 
        on_delete=models.CASCADE,
    )
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
    

class FocusBoat(models.Model):
    adopter = models.ForeignKey(
        Adopter, 
        null=True,
        blank=True,
        default=None,
        verbose_name=_("Adopter"), 
        on_delete=models.CASCADE,
    )
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']
    
    def __str__(self) -> str:
        return self.boat.name