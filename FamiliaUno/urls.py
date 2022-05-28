from django.contrib import admin
from django.urls import path

from FamiliaUno.views import prueba
from familiares.views import generar_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba, name = "prueba"),
    path('generar_familiar/', generar_familiar, name = "generar_familiar"),
]
