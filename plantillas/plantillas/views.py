from django.http import HttpResponse
from django.template import Template, Context


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
