from django.db import models


class Elon(models.Model):
    name = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='nomzod/', blank=True)
    nomzod = models.CharField(max_length=255)
    sana = models.DateField(auto_now_add=True)
    vaqt = models.IntegerField(blank=True)
    yoqish = models.BooleanField(default=False)   
    ovoz = models.CharField(max_length=100, blank=True) 
    baza = models.CharField(max_length=10, default='0')

class Baxo(models.Model):
    elon = models.ForeignKey(Elon, on_delete=models.CASCADE)
    baxo = models.CharField(max_length=200)
    baza = models.CharField(max_length=10, default='0')


class Statistika(models.Model):
    elon = models.ForeignKey(Elon, on_delete=models.CASCADE)
    rozilar = models.IntegerField(default=0)
    qarshilar = models.IntegerField(default=0)
    betaraf = models.IntegerField(default=0)
    qatnashmagan = models.IntegerField(default=0),
    rasm = models.ImageField(upload_to='statistika/')