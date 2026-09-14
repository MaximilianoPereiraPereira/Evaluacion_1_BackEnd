from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'index.html')

def mostrar_servicio(request):
    card = {
        "Nombre": "Lavado de Vehiculos",
        "Valor": 10000
    }

    return render(request, 'servicio.html', card)