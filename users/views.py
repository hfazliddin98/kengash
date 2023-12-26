from django.shortcuts import render, redirect
from ovoz.models import Baxo
from .models import Davomat


def qatnashmagan_son():
    qatnash = Davomat.objects.filter(aktiv=False)
    son = 0
    for b in qatnash:
        son += 1
    return son



def rozi_son():
    qatnash = Baxo.objects.filter(aktiv=False)
    son = 0
    for b in qatnash:
        son += 1
    return son

def qarshi_son():
    qatnash = Baxo.objects.filter(aktiv=False)
    son = 0
    for b in qatnash:
        son += 1
    return son
    
def betaraf_son():
    qatnash = Baxo.objects.filter(aktiv=False)
    son = 0
    for b in qatnash:
        son += 1
    return son

