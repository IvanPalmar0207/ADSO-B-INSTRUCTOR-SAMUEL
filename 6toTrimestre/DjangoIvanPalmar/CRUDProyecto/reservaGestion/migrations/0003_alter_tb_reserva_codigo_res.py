# Generated by Django 4.2.6 on 2023-12-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaGestion', '0002_tb_reserva_codigo_hab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_reserva',
            name='codigo_res',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo de la reserva'),
        ),
    ]