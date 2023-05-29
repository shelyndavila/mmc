from django import forms
from .models import Entrada,Proveedores,Productos,Clientes,Materiales, Barcos, ZonasFAO, ArtesPesca

class RegistrarEntrada(forms.Form):
    nombre_proveedor=forms.ModelChoiceField(label="Nombre Proveedor", queryset=Proveedores.objects.all())
    especie =forms.ModelChoiceField(label="Especie", queryset=Materiales.objects.all())
    cantidad_kg =forms.CharField(label="Cantidad en kg", required=False)
    cantidad_caja =forms.CharField(label="Cajas", required=False)
    precio_kg =forms.CharField(label="Precio", required=False)
    precio_caja =forms.CharField(label="Precio por caja", required=False)

    codigo_barco = forms.ModelChoiceField(label="Barco", queryset=Barcos.objects.all())
    codigo_zona =forms.ModelChoiceField(label="Zona FAO", queryset=ZonasFAO.objects.all())
    codigo_arte =forms.ModelChoiceField(label="Arte de Pesca", queryset=ArtesPesca.objects.all())





class RegistrarSalida(forms.Form):
    nombre_cliente=forms.ModelChoiceField(label="Nombre Cliente", queryset=Clientes.objects.all())
    especie=forms.ModelChoiceField(label="Especie", queryset=Productos.objects.all())
    cantidad_kg=forms.CharField(label="Cantidad en kg",required=False)
    cantidad_caja=forms.CharField(label="Cajas",required=False)
    precio_kg=forms.CharField(label="Precio",required=False)
    precio_caja=forms.CharField(label="Precio por caja",required=False)

