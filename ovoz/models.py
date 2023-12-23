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
    xal = models.BooleanField(default=False)
 
class Baxo(models.Model):
    user_id = models.CharField(max_length=10)
    taklif_id = models.CharField(max_length=10)
    xal = models.BooleanField(default=False)
    baxo = models.CharField(max_length=200)


class Statistika(models.Model):
    taklif_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    nomzod = models.CharField(max_length=255)
    rozilar = models.IntegerField(default=0)
    qarshilar = models.IntegerField(default=0)
    betaraflar = models.IntegerField(default=0)
    qatnashmaganlar = models.IntegerField(default=0)