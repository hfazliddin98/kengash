from django.contrib import admin
from .models import Taklif, Statistika


@admin.register(Taklif)
class TaklifAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Statistika)
class StatistikaAdmin(admin.ModelAdmin):
    list_display = ['id']