# Generated by Django 4.1.7 on 2023-04-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_entradas_entrada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=200)),
                ('especie', models.CharField(max_length=200)),
                ('cantidad_kg', models.CharField(blank=True, max_length=200)),
                ('cantidad_caja', models.CharField(blank=True, max_length=200)),
                ('precio_kg', models.CharField(blank=True, max_length=200)),
                ('precio_caja', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
