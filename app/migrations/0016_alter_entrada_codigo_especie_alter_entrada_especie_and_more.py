# Generated by Django 4.1.7 on 2023-05-10 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_entrada_codigo_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='codigo_especie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.materiales'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='especie',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='nombre_material',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
