# Generated by Django 4.1.7 on 2023-04-25 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_salida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materiales'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='nombre_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.proveedores'),
        ),
        migrations.AlterField(
            model_name='salida',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productos'),
        ),
        migrations.AlterField(
            model_name='salida',
            name='nombre_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes'),
        ),
    ]
