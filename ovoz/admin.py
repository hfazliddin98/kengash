from django.contrib import admin
from .models import Elon, Statistika


@admin.register(Elon)
class ElonAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Statistika)
class StatistikaAdmin(admin.ModelAdmin):
    list_display = ['id']