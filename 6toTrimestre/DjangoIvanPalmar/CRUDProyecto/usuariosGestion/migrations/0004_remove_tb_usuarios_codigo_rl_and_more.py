# Generated by Django 4.2.6 on 2023-11-13 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuariosGestion', '0003_rename_tb_usuario_tb_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_usuarios',
            name='codigo_rl',
        ),
        migrations.RemoveField(
            model_name='tb_usuarios',
            name='codigo_tpD',
        ),
    ]
