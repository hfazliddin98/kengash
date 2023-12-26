from django.contrib import admin
from .models import Taklif, Statistika, Baxo


@admin.register(Taklif)
class TaklifAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Statistika)
class StatistikaAdmin(admin.ModelAdmin):
    list_display = ['id','taklif_id', 'xal']

@admin.register(Baxo)
class BaxoAdmin(admin.ModelAdmin):
    list_display = ['id']