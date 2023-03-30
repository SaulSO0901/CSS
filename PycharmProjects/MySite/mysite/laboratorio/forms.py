from django import forms
from .models import Personal,Equipo,Prestamo


class FormularioEquipos(forms.ModelForm):
    class meta:
        model = Equipo
        field=["nombre","descripcion"]