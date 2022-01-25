from django.db.models import fields
from app.models.pago import Pago
from rest_framework import serializers


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['tipo_pago']
