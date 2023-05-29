from django.contrib import admin
from .models import Clientes, Proveedores, Productos, Materiales, Entrada,Salida

# Register your models here.
admin.site.register(Entrada)
admin.site.register(Proveedores)
admin.site.register(Materiales)
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Salida)
