from django.shortcuts import render, redirect, get_object_or_404
from .models import instrumentos,ventas
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    Ventas = ventas.objects.all()
    context = {
        "ventas":ventas
    }
    return render(request,"Index.html", context)