from django.http import HttpResponse


def hello(request):  # primera vista (todas las funciones en este archivo se denominan vistas)

    return HttpResponse("Buen día para aprender Django")


def goodbye(request):
    return HttpResponse("Disfrútalo, la vida son dos días.")
