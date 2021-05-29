from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render


def hello(request):
    doc_externo = open(
        "C:/Users/NITROPC/Documents/My-Code/pildoras/python/DJango/plantillas/plantillas/plantillasHtml/first.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)


def helloCtx(request):
    nombre = "Pepito"
    doc_externo = open(  # Ojo con las barras estilo linux al cargar plantilla
        "C:/Users/NITROPC/Documents/My-Code/pildoras/python/DJango/plantillas/plantillas/plantillasHtml/second.html")
# 1ºCreamos un template
    plt = Template(doc_externo.read())
# 2º Cerramos archivo abierto
    doc_externo.close()
# 3º creamos un ctx
    ctx = Context({"nombre_persona": nombre})
# 4º renderizamos
    documento = plt.render(ctx)

    return HttpResponse(documento)


def actualTime(request):
    time = datetime.now()
    doc_externo = open(
        "C:/Users/NITROPC/Documents/My-Code/pildoras/python/DJango/plantillas/plantillas/plantillasHtml/time.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"time": time})
    documento = plt.render(ctx)
    return HttpResponse(documento)


class Persona(object):

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


def clasesData(request):

    p1 = Persona("Don Iago", "Ubeira")
    doc_externo = open(
        "C:/Users/NITROPC/Documents/My-Code/pildoras/python/DJango/plantillas/plantillas/plantillasHtml/class.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre": p1.nombre, "apellido": p1.apellido})
    documento = plt.render(ctx)
    return HttpResponse(documento)


def listas(request):
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas"]

    doc_externo = open(
        "C:/Users/NITROPC/Documents/My-Code/pildoras/python/DJango/plantillas/plantillas/plantillasHtml/listas.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"temas": temas})
    documento = plt.render(ctx)
    return HttpResponse(documento)


# Increíble, cuatro líneas hace todo lo anterior...


def doingShortcuts(request):
    p1 = Persona("Don Iago", "Ubeira")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas"]
    time = datetime.now()

    return render(request, "shortcuts.html", {"nombre": p1.nombre, "apellido": p1.apellido, "temas": temas, "time": time})


def herencias(request):
    time = datetime.now()

    return render(request, "./herencias/CursoC.html", {"dameFecha": time})


def herencia2(request):
    time = datetime.now()

    return render(request, "./herencias/CursoB.html", {"dameFecha": time})
