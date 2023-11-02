from django.urls import path
from inicio.views import inicio,crear_caña, caña_de_pescar, crear_reels, reels, crear_señuelo, señuelo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reels/', reels, name='reels'),
    path('reels/crear-reels/', crear_reels, name='crear_reels'),
    path('cañas/', caña_de_pescar, name='cañas'),
    path('cañas/Crear-caña/', crear_caña, name='crear_caña'),
    path('señuelos/', señuelo, name='señuelos'),
    path('señuelo/crear-señuelo/', crear_señuelo, name='crear_señuelo')
]
