# Generated by Django 4.1.7 on 2023-05-05 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_entrada_fecha_alter_salida_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='codigo_proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Entrada_codigo_proveedor', to='app.proveedores'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='nombre_proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Entrada_nombre_proveedor', to='app.proveedores'),
        ),
    ]
