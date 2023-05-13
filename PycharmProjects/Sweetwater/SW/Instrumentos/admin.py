from django.contrib import admin

# Register your models here.
from .models import instrumentos,ventas
admin.site.register(instrumentos)
admin.site.register(ventas)