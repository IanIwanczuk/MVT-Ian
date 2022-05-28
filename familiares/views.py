from django.shortcuts import render

from familiares.models import Familiares

# Create your views here.
def familiares(request):
    famliar_nuevo = Familiares.objects.create(
            nombre = "Ian",
            apellido = "Iwanczuk",
            nacimiento = "02/10/2022",
            edad = "19",
            )
    context = {'familiar_nuevo': famliar_nuevo}
    return render(request, 'familiares.html', context=context)