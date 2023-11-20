from django.contrib import admin
from django.urls import path
from .views import HomeView, StatistikaView, TaklifView, ElonView, AzoView, YoqishView, pie_chart

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('statistika/', StatistikaView.as_view(), name='statistika'),
    path('taklif/', TaklifView.as_view(), name='taklif'),
    path('elon/', ElonView.as_view(), name='elon'),
    path('azo/', AzoView.as_view(), name='azo'),
    path('pie_chart/<int:pk>/', pie_chart, name='pie_chart'),
    path('yoqish/<int:pk>/', YoqishView.as_view(), name='yoqish'),
]