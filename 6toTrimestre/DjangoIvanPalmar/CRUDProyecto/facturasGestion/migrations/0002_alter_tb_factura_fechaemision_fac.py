# Generated by Django 4.2.6 on 2023-12-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturasGestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_factura',
            name='fechaEmision_fac',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de emision de la factura'),
        ),
    ]