# Generated by Django 4.1.7 on 2023-05-22 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_entrada_fecha_captura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_captura',
            field=models.DateField(default=datetime.date),
        ),
    ]
