from django.db import models
from django.db.models.fields import AutoField
from .reserva import Reserva


class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(
        Reserva, null=False, blank=False, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=50, null=False, blank=False)
