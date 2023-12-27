from django.shortcuts import render, redirect
from ovoz.models import Baxo, Taklif
from .models import Davomat, User


def home_azolar_soni():
    try:
        data = User.objects.filter(lavozim='azo')
        son = 0
        for d in data:
           son += 1
        return son
    except:
        son = 0
        return son

def home_takliflar_soni():
    try:
        data = Taklif.objects.all()
        son = 0
        for d in data:
           son += 1
        return son
    except:
        son = 0
        return son

def home_aktiv_takliflar_soni():
    try:
        data = Taklif.objects.filter(yoqish=True)
        son = 0
        for d in data:
           son += 1
        return son
    except:
        son = 0
        return son

def home_baholangan_takliflar_soni():
    try:
        data = Taklif.objects.filter(tugash=True)
        son = 0
        for d in data:
           son += 1
        return son
    except:
        son = 0
        return son


def statistika_rozilar_soni():
    try:
        qatnash = Baxo.objects.filter(baxo="roziman")
        son = 0
        for b in qatnash:
            son += 1
        return son
    except:
        son = 0
        return son

def statistika_qarshilar_soni():
    try:
        qatnash = Baxo.objects.filter(baxo="qarshiman")
        son = 0
        for b in qatnash:
            son += 1
        return son
    except:
        son = 0
        return son
    
def statistika_betaraflar_soni():
    try:
        qatnash = Baxo.objects.filter(baxo='betarafman')
        son = 0
        for b in qatnash:
            son += 1
        return son
    except:
        son = 0
        return son
    

def statistika_qatnashmaganlar_soni():    
    try:
        qatnash = Davomat.objects.filter(aktiv=False)
        son = 0
        for b in qatnash:
            son += 1
        print(son)
        return son
    except:
        son = 0
        return son

