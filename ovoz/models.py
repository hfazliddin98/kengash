from django.db import models
from users.models import User


class Taklif(models.Model):
    name = models.CharField(max_length=255)
    nomzod = models.CharField(max_length=255)
    vaqt = models.IntegerField(blank=True)
    boshlanish_vaqti = models.CharField(max_length=100, blank=True)
    tugash_vaqti = models.CharField(max_length=100, blank=True)
    yoqish = models.BooleanField(default=False)   
    tugash = models.BooleanField(default=False)
 
class Baxo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    taklif_id = models.ForeignKey(Taklif, on_delete=models.CASCADE)
    baxo = models.CharField(max_length=200)


class Statistika(models.Model):
    elon = models.ForeignKey(Taklif, on_delete=models.CASCADE)
    rozilar = models.IntegerField(default=0)
    qarshilar = models.IntegerField(default=0)
    betaraf = models.IntegerField(default=0)
    qatnashmagan = models.IntegerField(default=0)
    rasm = models.ImageField(upload_to='statistika/')