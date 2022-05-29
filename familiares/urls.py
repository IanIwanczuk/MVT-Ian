from django.urls import path

from familiares.views import generar_familiar, mostrar_familia

urlpatterns = [
    path('generar_familiar/', generar_familiar, name = "generar_familiar"),
    path('mostrar_familia/', mostrar_familia, name = "mostrar_familia"),
]
