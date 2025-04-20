from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    otp = models.CharField(max_length=6, null=True, blank=True)
