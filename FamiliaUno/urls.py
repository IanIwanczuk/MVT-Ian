from django.contrib import admin
from django.urls import path, include

from FamiliaUno.views import prueba, index

urlpatterns = [
    path('index/', index, name = "index"),
    path('admin/', admin.site.urls),
    path('prueba/', prueba, name = "prueba"),

    path('familia/', include('familiares.urls')),
]
