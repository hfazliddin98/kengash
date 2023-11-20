from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import RoyhatView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('royhat/', RoyhatView.as_view(), name='royhat'),
]