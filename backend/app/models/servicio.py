from django.db import models
from .reserva import Reserva


class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(
        Reserva, null=False, blank=False, on_delete=models.CASCADE)
    nombreServicio = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    precioDia = models.IntegerField(null=False, blank=False)
