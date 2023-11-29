from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Lavozim = (
        ('admin', 'Admin'),
        ('azo', 'Azo')
    )
    lavozim = models.CharField(max_length=100, choices=Lavozim)


class Davomat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bor = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)