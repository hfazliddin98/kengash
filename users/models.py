from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Lavozim = (
        ('admin', 'Admin'),
        ('azo', 'Azo')
    )
    lavozim = models.CharField(max_length=100, choices=Lavozim)