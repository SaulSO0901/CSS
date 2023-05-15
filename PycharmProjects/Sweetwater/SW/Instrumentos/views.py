from django.shortcuts import render, redirect, get_object_or_404
from .models import instrumentos,ventas
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    Ventas = ventas.objects.all()
    context = {
        "ventas":Ventas
    }
    return render(request,"Index.html", context)

def Guitarra(request):
    Ventas = ventas.objects.all()
    context = {
        "Ventas":Ventas
    }
    return render(request,"Guitarra.html", context)

def RV(request):
    if request.method == 'POST':
        Ventas = ventas()
        Ventas.idventa = request.POST.get('ID')
        Ventas.Total = request.POST.get('Total')
        Ventas.Fecha = request.POST.get('Fecha')
        Ventas.save()
        return JsonResponse(["Listo"], safe=False)