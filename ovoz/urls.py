from django.contrib import admin
from django.urls import path
from .views import HomeView, StatistikaView, TaklifView, ElonView, AzoView, YoqishView, \
    TakliflarAzoView, RozilarView, QarshilarView, BetaraflarView, DavomatView, davomatlar
from .views import pie_chart

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('statistika/', StatistikaView.as_view(), name='statistika'),
    path('taklif/', TaklifView.as_view(), name='taklif'),
    path('elon/', ElonView.as_view(), name='elon'),
    path('azo/', AzoView.as_view(), name='azo'),
    path('pie_chart/<int:pk>/', pie_chart, name='pie_chart'),
    path('yoqish/<int:pk>/', YoqishView.as_view(), name='yoqish'),
    path('taklif_azo/', TakliflarAzoView.as_view(), name='taklif_azo'),
    path('rozilar/<int:pk>/', RozilarView.as_view(), name='rozilar'),
    path('qarshilar/<int:pk>/', QarshilarView.as_view(), name='qarshilar'),
    path('betaraflar/<int:pk>/', BetaraflarView.as_view(), name='betaraflar'),
    path('davomat/', DavomatView.as_view(), name='davomat'),
    path('davomatlar/<int:pk>/', davomatlar, name='davomatlar')
]