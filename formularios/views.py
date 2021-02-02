from django.shortcuts import render
from django.http import HttpResponse


def formulario(request):
    return render(request, 'formularios.html')

def buscar(request):
    if request.POST["operador"] == "Sumar/restar":
        n1 = request.POST["numero1"]
        n2 = request.POST["numero2"]
        if n1 == "" and n2 == "" or n1 == "" or n2 == "":
            nom = "sin valor"
            return render(request, "buscar.html", {"Nombre":nom})
        else:
            sumres = int(n1) + int(n2)
            return render(request, "buscar.html", {"sumres":sumres})
    elif request.POST["operador"] == "Dividir":
        n1 = request.POST["numero1"]
        n2 = request.POST["numero2"]
        if n1 == "" and n2 == "" or n1 == "" or n2 == "":
            nom = "sin valor"
            return render(request, "buscar.html", {"Nombre":nom})
        else:
            try:
                div = int(n1) / int(n2)
                return render(request, "buscar.html", {"division":div})
            except ZeroDivisionError:
                div = "Error"
                return render(request, "buscar.html", {"division":div})