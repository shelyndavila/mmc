# Generated by Django 4.1.7 on 2023-05-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_salida_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtesPesca',
            fields=[
                ('codigo_arte', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('nombre_arte', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Artes de Pesca',
            },
        ),
        migrations.CreateModel(
            name='Barcos',
            fields=[
                ('codigo_barco', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('nombre_barco', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Barcos',
            },
        ),
        migrations.CreateModel(
            name='ZonasFAO',
            fields=[
                ('codigo_zona', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('nombre_zona', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Zonas FAO',
            },
        ),
    ]
