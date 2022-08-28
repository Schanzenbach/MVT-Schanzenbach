from cgitb import text
from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiar(request):
    hermano=Familiar(nombre="Alexis", apellido="Kriger", DNI=12345678, fecha_nacimiento="1993-05-04")
    hermana=Familiar(nombre="Ailen", apellido="Schanzenbach", DNI=12345677, fecha_nacimiento="1996-06-29")
    madre=Familiar(nombre="Sonia", apellido="Kriger", DNI=12345676, fecha_nacimiento="1974-10-16")
    hermano.save()
    hermana.save()
    madre.save()
    diccionario={"Hermano": hermano, "Hermana": hermana, "Madre": madre}
    plantilla=loader.get_template("plantilladesafio6.html")
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)

