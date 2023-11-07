from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    nombreCompleto = models.CharField(max_length=80)
    numeroDocumento = models.IntegerField()
    numeroFicha = models.CharField(max_length=50)
    aprendizFoto = models.ImageField(upload_to='fotosAprendices')

    def __str__(self):
        return f'El nombre del aprendiz es: {self.nombreCompleto}, el numero de documento es: {self.numeroDocumento} y el numero de ficha es: {self.numeroFicha}'