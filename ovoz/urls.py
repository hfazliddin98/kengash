from django.contrib import admin
from django.urls import path
from .views import taklif_kiritish, taklif, azolar, taklif_azo, davomat, bor, yoq
from .views import davomat_yangilash, taklif_yoqish, taklif_ochirish, statistika
from .views import diyogramma, roziman, qarshiman, betarafman, kirish, home, azo_qoshish


urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('statistika/', statistika, name='statistika'),
    path('taklif/', taklif, name='taklif'),
    path('taklif_kiritish/', taklif_kiritish, name='taklif_kiritish'),
    path('azolar/', azolar, name='azolar'),
    path('diyogramma/<int:pk>/', diyogramma, name='diyogramma'),
    path('yoqish/<int:pk>/', taklif_yoqish, name='yoqish'),
    path('ochirish/<int:pk>/', taklif_ochirish, name='ochirish'),
    path('taklif_azo/', taklif_azo, name='taklif_azo'),
    path('azo_qoshish/', azo_qoshish, name='azo_qoshish'),
    path('roziman/<int:pk>/', roziman, name='roziman'),
    path('qarshiman/<int:pk>/', qarshiman, name='qarshiman'),
    path('betarafman/<int:pk>/', betarafman, name='betarafman'),
    path('davomat/', davomat, name='davomat'),
    path('bor/<int:pk>/', bor, name='bor'),
    path('yoq/<int:pk>/', yoq, name='yoq'),
    path('davomat_yangilash/', davomat_yangilash, name='davomat_yangilash'),
]