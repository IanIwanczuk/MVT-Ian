from django.contrib import admin
from django.urls import path

from FamiliaUno.views import prueba
from familiares.views import familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba, name = "prueba"),
    path('familiares/', familiares, name = "familiares"),
]
