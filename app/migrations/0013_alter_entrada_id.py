# Generated by Django 4.1.7 on 2023-05-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_entrada_codigo_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
