from django.urls import path
from inicio.views import inicio,crear_caña, caña_de_pescar, crear_reels, reels, crear_señuelo, señuelo, DetalleCaña, ActualizarCaña, EliminarCaña

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reels/', reels, name='reels'),
    path('reels/crear-reels/', crear_reels, name='crear_reels'),
    path('cañas/', caña_de_pescar, name='cañas'),
    path('cañas/Crear-caña/', crear_caña, name='crear_caña'),
    path('señuelos/', señuelo, name='señuelos'),
    path('señuelo/crear-señuelo/', crear_señuelo, name='crear_señuelo'),
    path('cañas/<int:pk>/detalle/', DetalleCaña.as_view() , name = 'detalle_caña'),
    path('cañas/<int:pk>/actualizar/', ActualizarCaña.as_view() , name = 'actualizar_caña'),
    path('cañas/<int:pk>/eliminar/', EliminarCaña.as_view() , name = 'eliminar_caña')
]
