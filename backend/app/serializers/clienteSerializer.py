from django.db.models import fields
from django.utils.translation import activate
from app.models.cliente import Cliente
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["active"]
