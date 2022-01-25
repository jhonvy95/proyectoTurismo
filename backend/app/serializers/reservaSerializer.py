from django.db.models import fields
from app.models.reserva import Reserva
from rest_framework import serializers


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['fechaReserva', 'fechaIngreso', 'fechaSalida', 'costo']

    def to_representation(self, obj):
        reserva = Reserva.objects.get(idReserva=obj.idReserva)

        return{

            "reserva": {
                "fechaReserva": reserva.fechaReserva,
                "fechaIngreso": reserva.fechaIngreso,
                "fechaSalida": reserva.fechaSalida,
                "costo": reserva.costo
            }
        }
