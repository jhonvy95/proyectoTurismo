from django.db import models


class Persona(models.Model):
    documento = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(null=False)
    correo = models.EmailField(null=False)
