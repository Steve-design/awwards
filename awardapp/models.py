from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='images/', blank=True)
    bio = HTMLField()
    contact = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save_profile(self):
        self.save()