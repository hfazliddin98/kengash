from django.contrib import admin
from django.urls import path
from .views import HomeView, StatistikaView, TaklifKiritishView, TaklifView, AzoView, \
    TakliflarAzoView, DavomatView, bor, yoq, \
    davomat_yangilash, taklif_yoqish, taklif_ochirish
from .views import diyogramma, roziman, qarshiman, betarafman, kirish


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
    path('roziman/<int:pk>/', roziman, name='roziman'),
    path('qarshiman/<int:pk>/', qarshiman, name='qarshiman'),
    path('betarafman/<int:pk>/', betarafman, name='betarafman'),
    path('davomat/', DavomatView.as_view(), name='davomat'),
    path('bor/<int:pk>/', bor, name='bor'),
    path('yoq/<int:pk>/', yoq, name='yoq'),
    path('kirish/', kirish, name='kirish'),
    path('davomat_yangilash/', davomat_yangilash, name='davomat_yangilash'),
]