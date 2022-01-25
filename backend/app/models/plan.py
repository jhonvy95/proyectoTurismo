from django.db import models
from .reserva import Reserva


class Plan(models.Model):
    idPlan = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(
        Reserva, null=False, blank=False, on_delete=models.CASCADE)
    tipoPlan = models.CharField(max_length=200, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
