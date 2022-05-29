from django.shortcuts import render

from familiares.models import Familiares

# Create your views here.
def generar_familiar(request):
    famliar_nuevo = Familiares.objects.create(
        nombre = "María",
        apellido = "Han",
        nacimiento = "08/25/2028",
        edad = "23",
        )
    context = {'familiar_nuevo': famliar_nuevo}
    return render(request, 'familiares.html', context=context)

def mostrar_familia(request):
        miembros_familia = Familiares.objects.all()
        context = {'Familia':miembros_familia}
        return render(request, 'mostrar_familia.html', context=context)