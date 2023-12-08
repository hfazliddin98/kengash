from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Lavozim = (
        ('admin', 'Admin'),
        ('azo', 'Azo')
    )
    lavozim = models.CharField(max_length=100, choices=Lavozim)


class Davomat(models.Model):
    user_id = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    ism = models.CharField(max_length=100)
    aktiv = models.BooleanField(default=False)
    sana = models.CharField(max_length=100, blank=True)