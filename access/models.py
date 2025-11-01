from django.contrib.auth.models import User
from django.db import models
from monitoring.models import Adopter
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adopter = models.ForeignKey(
        Adopter, 
        verbose_name=_("Adopter"), 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
