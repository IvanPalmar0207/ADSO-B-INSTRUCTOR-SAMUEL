from django.db import models

# Create your models here.

class tb_tipoHabitacion(models.Model):
    codigo_tpH = models.AutoField(primary_key=True, verbose_name='Codigo del tipo de habitacion')
    tipo_tpH = models.CharField(max_length=70,verbose_name='Tipo de habitacion')
    valorBase_tpH = models.FloatField(verbose_name='Valor base del tipo de habitacion')

class tb_mobiliario(models.Model):
    codigo_tpH = models.ForeignKey("tb_tipoHabitacion", verbose_name="Codigo del tipo de habitacion", on_delete=models.CASCADE)
    camasSecillas_im = models.IntegerField(verbose_name='Numero de camas sencillas')
    camasDobles_im = models.IntegerField(verbose_name='Numero de camas dobles')
    camasTriples_im = models.IntegerField(verbose_name='Numero de camas triples')
    camasMatrimoniales_im = models.IntegerField(verbose_name='Numero de camas matrimoniales')
    televisor_im = models.IntegerField(verbose_name='Numero de televisores')
    bano_im = models.IntegerField(verbose_name='Numero de baños')
    escritorio_im = models.IntegerField(verbose_name='Numero de escritorios')
    
class tb_habitacion(models.Model):
    codigo_hab = models.IntegerField(primary_key=True, verbose_name='Codigo de la habitacion')
    codigo_tpH = models.ForeignKey("tb_tipoHabitacion", verbose_name="Codigo del tipo de habitacion", on_delete=models.CASCADE)
    precio_tpH = models.FloatField(verbose_name='Precio de la habitacion')
    descripcion_tpH = models.TextField(verbose_name='Descripcion de la habitacion')
    minimoPersonas_tpH = models.IntegerField(verbose_name='Minimo de personas')
    maximoPersonas_tpH = models.IntegerField(verbose_name='Maximo de personas')
    image_tpH = models.ImageField(upload_to='fotoHabitaciones')