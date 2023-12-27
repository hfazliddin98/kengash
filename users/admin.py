from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Davomat

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ['id', 'aktiv']