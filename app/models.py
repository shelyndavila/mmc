import datetime
from django.db import models


# Create your models here.
class Clientes(models.Model):
    codigo_cliente=models.CharField(max_length=300,primary_key=True) #QUERIA PONER NUMERO PERO NO SE IntegerField(primary_key=True)     #
    nombre_cliente=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre_cliente
    class Meta:
        verbose_name_plural = "Clientes"
class ArtesPesca(models.Model):
    codigo_arte=models.CharField(max_length=300,primary_key=True) #QUERIA PONER NUMERO PERO NO SE IntegerField(primary_key=True)     #
    nombre_arte=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre_arte
    class Meta:
        verbose_name_plural = "Artes de Pesca"
class ZonasFAO(models.Model):
    codigo_zona=models.CharField(max_length=300,primary_key=True) #QUERIA PONER NUMERO PERO NO SE IntegerField(primary_key=True)     #
    nombre_zona=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre_zona
    class Meta:
        verbose_name_plural = "Zonas FAO"
class Barcos(models.Model):
    codigo_barco=models.CharField(max_length=300,primary_key=True) #QUERIA PONER NUMERO PERO NO SE IntegerField(primary_key=True)     #
    nombre_barco=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre_barco
    class Meta:
        verbose_name_plural = "Barcos"
class Proveedores(models.Model):
    codigo_proveedor=models.CharField(max_length=300,primary_key=True)
    nombre_proveedor=models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.nombre_proveedor
    class Meta:
        verbose_name_plural = "Proveedores"
class Materiales(models.Model):
    codigo_material=models.CharField(max_length=300,primary_key=True)
    nombre_material=models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.nombre_material

    class Meta:
        verbose_name_plural = "Materiales"
class Productos(models.Model):
    codigo_producto=models.CharField(max_length=300,primary_key=True)
    nombre_producto=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre_producto
    class Meta:
        verbose_name_plural = "Productos"
class Entrada(models.Model):
    id=models.AutoField(primary_key=True)
    lote = models.CharField(max_length=50, default='',blank=True, null=True)
    codigo_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, null=True, blank=True)
    nombre_proveedor = models.CharField(max_length=300, null=True, blank=True)
    codigo_especie = models.ForeignKey(Materiales, on_delete=models.CASCADE, null=True, blank=True)
    especie = models.CharField(max_length=300, null=True, blank=True)
    cantidad_kg=models.CharField(max_length=200, blank=True)
    cantidad_caja=models.CharField(max_length=200, blank=True)
    precio_kg=models.CharField(max_length=200, blank=True)
    precio_caja=models.CharField(max_length=200, blank=True)
    fecha=models.DateField(default=datetime.date.today)
    albaran=models.CharField(max_length=50, default='',blank=True, null=True)
    codigo_zona=models.ForeignKey(ZonasFAO, on_delete=models.CASCADE, null=True, blank=True)
    codigo_arte=models.ForeignKey(ArtesPesca, on_delete=models.CASCADE, null=True, blank=True)
    fecha_captura=models.DateField(default=datetime.date.today)
    codigo_barco=models.ForeignKey(Barcos, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.nombre_proveedor)

    class Meta:
        verbose_name_plural = "Entradas"
class Salida(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_cliente_id=models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, blank=True)
    nombre_cliente=models.CharField(max_length=300, null=True, blank=True)
    codigo_especie_id=models.ForeignKey(Productos,on_delete=models.CASCADE, null=True, blank=True)
    especie=models.CharField(max_length=300, null=True, blank=True)
    cantidad_kg=models.CharField(max_length=200, blank=True)
    cantidad_caja=models.CharField(max_length=200, blank=True)
    precio_kg=models.CharField(max_length=200, blank=True)
    precio_caja=models.CharField(max_length=200, blank=True)
    fecha=models.DateField(default=datetime.date.today)
    def __str__(self):
        return str(self.nombre_cliente)
    class Meta:
        verbose_name_plural = "Salidas"   