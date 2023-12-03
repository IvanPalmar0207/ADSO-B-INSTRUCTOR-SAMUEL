# Generated by Django 4.2.7 on 2023-11-28 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuariosAPI', '0001_initial'),
        ('habitacionesGestion', '0002_remove_tb_habitacion_precio_tph'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_reserva',
            fields=[
                ('codigo_res', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero de la reserva')),
                ('fechaInicio_res', models.DateField(verbose_name='Fecha de inicio')),
                ('fechaSalida_res', models.DateField(verbose_name='Fecha de salida')),
                ('cantidadJovenes_res', models.IntegerField(verbose_name='Cantidad de jovenes')),
                ('cantidadAdultos_res', models.IntegerField(verbose_name='Cantidad de adultos')),
                ('codigo_hab', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='habitacionesGestion.tb_habitacion', verbose_name='Codigo de la habitacion')),
                ('numeroDocumento_cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuariosAPI.tb_usuarios', verbose_name='Numero de documento del usuario')),
            ],
        ),
    ]