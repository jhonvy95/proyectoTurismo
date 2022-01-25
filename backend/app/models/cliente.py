from django.db import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from .persona import Persona


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    documento_persona = models.ForeignKey(
        Persona, null=False, blank=False, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
