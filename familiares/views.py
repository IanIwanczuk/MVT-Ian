from django.shortcuts import render

from familiares.models import Familiares

# Create your views here.
def generar_familiar(request):
    famliar_nuevo = Familiares.objects.create(
            nombre = "Roberto",
            apellido = "Milan",
            nacimiento = "12/14/2006",
            edad = "45",
            )
    context = {'familiar_nuevo': famliar_nuevo}
    return render(request, 'familiares.html', context=context)