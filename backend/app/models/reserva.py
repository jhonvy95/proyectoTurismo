from django.db import models
from django.db.models.fields import DateField
from .cliente import Cliente


class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(
        Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fechaReserva = models.DateField(null=False, blank=False)
    fechaIngreso = models.DateField(null=False, blank=False)
    fechaSalida = models.DateField(null=False, blank=False)
    costo = models.IntegerField()
