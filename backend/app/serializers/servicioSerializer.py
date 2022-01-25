from django.db.models import fields
from app.models.servicio import Servicio
from rest_framework import serializers


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['nombreServicio', 'descripcion', 'precioDia']
