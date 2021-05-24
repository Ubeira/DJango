from datetime import datetime
from django.http import HttpResponse


def hello(request):  # primera vista (todas las funciones en este archivo se denominan vistas)
    documento = """
    <html>
        <body>
            <h1>Buen día para aprender Django</h1>
        </body>
    </html>
    """
    return HttpResponse(documento)


def goodbye(request):
    return HttpResponse("Disfrútalo, la vida son dos días.")


def getData(request):

    now = datetime.now()
    documento = """
    <html>
        <body>
            <h1>
                Fecha y hora actuales:
            </h1>
            <h3> %s</h3>
        </body>
    </html>
    """ % now
    return HttpResponse(documento)


def getAge(request, age, year):

    time = year-2021
    futureAge = age+time
    document = """
        <html>
            <body>
                <h2>
                    En el año %s tendrás %s años
                </h2>
            </body>
        </html>
    """ % (year, futureAge)

    return HttpResponse(document)
