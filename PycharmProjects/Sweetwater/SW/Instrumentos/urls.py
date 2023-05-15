from django.urls import path

# Create your views here.
from . import views

urlpatterns = [
    
    path("", views.Guitarra, name="Guitarra"),
path("Registro", views.RV, name="Registro"),
]
