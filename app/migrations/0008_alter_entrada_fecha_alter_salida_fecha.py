# Generated by Django 4.1.7 on 2023-05-05 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_clientes_options_alter_entrada_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
