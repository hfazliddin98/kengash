from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Lavozim = (
        ('admin', 'admin'),
        ('azo', 'azo')
    )
    lavozim = models.CharField(max_length=100, choices=Lavozim)
    parol = models.CharField(max_length=100)