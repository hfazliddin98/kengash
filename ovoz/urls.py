from django.contrib import admin
from django.urls import path
from .views import taklif_kiritish, taklif, azolar, taklif_azo, davomat, bor, yoq, stistika_yangilanishi
from .views import davomat_yangilash, taklif_yoqish, taklif_ochirish, statistika, xal_qilish
from .views import diyogramma, roziman, qarshiman, betarafman, kirish, home, azo_qoshish, taklif_azo_baxolash


urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('statistika/', statistika, name='statistika'),
    path('stistika_yangilanishi/', stistika_yangilanishi, name='stistika_yangilanishi'),
    path('taklif/', taklif, name='taklif'),
    path('taklif_kiritish/', taklif_kiritish, name='taklif_kiritish'),
    path('azolar/', azolar, name='azolar'),
    path('diyogramma/<int:pk>/', diyogramma, name='diyogramma'),
    path('yoqish/<int:pk>/', taklif_yoqish, name='yoqish'),
    path('ochirish/<int:pk>/', taklif_ochirish, name='ochirish'),
    path('taklif_azo/', taklif_azo, name='taklif_azo'),
    path('taklif_azo_baxolash/<int:pk>/', taklif_azo_baxolash, name='taklif_azo_baxolash'),
    path('azo_qoshish/', azo_qoshish, name='azo_qoshish'),
    path('roziman/<int:pk>/', roziman, name='roziman'),
    path('qarshiman/<int:pk>/', qarshiman, name='qarshiman'),
    path('betarafman/<int:pk>/', betarafman, name='betarafman'),
    path('davomat/', davomat, name='davomat'),
    path('bor/<int:pk>/', bor, name='bor'),
    path('yoq/<int:pk>/', yoq, name='yoq'),
    path('davomat_yangilash/', davomat_yangilash, name='davomat_yangilash'),
    path('xal_qilish/<int:pk>/', xal_qilish, name='xal_qilish'),
]