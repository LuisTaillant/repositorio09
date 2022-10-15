from django.urls import path
# from .views import hola, fecha
from home import views
# from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('hola/', views.hola, name='hola'),
    # path('fecha/', views.fecha, name='fecha'),
    # path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    # path('mi-template/', views.mi_template, name='mi_template'),
    # path('mi-template/<str:nombre>', views.tu_template),
    # path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),
    # path('hola/', hola),
    # path('fecha/', fecha),
]