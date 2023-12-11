from django.contrib import admin
from django.urls import path
from .views import HomeView, StatistikaView, TaklifKiritishView, TaklifView, AzoView, \
    TakliflarAzoView, RozilarView, QarshilarView, BetaraflarView, DavomatView, bor, yoq, \
    davomat_yangilash, taklif_yoqish, taklif_ochirish
from .views import diyogramma
from .vaqt import tugatish


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('statistika/', StatistikaView.as_view(), name='statistika'),
    path('taklif/', TaklifView.as_view(), name='taklif'),
    path('taklif_kiritish/', TaklifKiritishView.as_view(), name='taklif_kiritish'),
    path('azo/', AzoView.as_view(), name='azo'),
    path('diyogramma/<int:pk>/', diyogramma, name='diyogramma'),
    path('yoqish/<int:pk>/', taklif_yoqish, name='yoqish'),
    path('ochirish/<int:pk>/', taklif_ochirish, name='ochirish'),
    path('taklif_azo/', TakliflarAzoView.as_view(), name='taklif_azo'),
    path('rozilar/<int:pk>/', RozilarView.as_view(), name='rozilar'),
    path('qarshilar/<int:pk>/', QarshilarView.as_view(), name='qarshilar'),
    path('betaraflar/<int:pk>/', BetaraflarView.as_view(), name='betaraflar'),
    path('davomat/', DavomatView.as_view(), name='davomat'),
    path('bor/<int:pk>/', bor, name='bor'),
    path('yoq/<int:pk>/', yoq, name='yoq'),
    path('davomat_yangilash/', davomat_yangilash, name='davomat_yangilash'),
    path('tugatish/<int:pk>/', tugatish, name='tugatish'),
]