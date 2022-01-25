from django.db.models import fields

# Import Models
from app.models.persona import Persona
from app.models.cliente import Cliente
from app.models.reserva import Reserva
from app.models.plan import Plan
from app.models.pago import Pago
from app.models.servicio import Servicio

# import serializer
from rest_framework import serializers
from app.serializers.clienteSerializer import ClienteSerializer
from app.serializers.reservaSerializer import ReservaSerializer
from app.serializers.planSerializer import PlanSerializer
from app.serializers.pagoSerializer import PagoSerializer
from app.serializers.servicioSerializer import ServicioSerializer


class PersonaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    reserva = ReservaSerializer()
    plan = PlanSerializer()
    pago = PagoSerializer()
    servicio = ServicioSerializer()

    class Meta:
        model = Persona
        fields = ['documento', 'nombres', 'apellidos',
                  'telefono', 'correo', 'cliente', 'reserva', 'plan', 'pago', 'servicio']

    def create(self, validated_data):
        clienteData = validated_data.pop('cliente')
        reservaData = validated_data.pop('reserva')
        planData = validated_data.pop('plan')
        pagoData = validated_data.pop('pago')
        servicioData = validated_data.pop('servicio')

        personaInstance = Persona.objects.create(**validated_data)
        clienteInstance = Cliente.objects.create(
            documento_persona=personaInstance, **clienteData)
        reservaInstance = Reserva.objects.create(
            id_cliente=clienteInstance, **reservaData)
        Plan.objects.create(
            id_reserva=reservaInstance, **planData)
        Pago.objects.create(
            id_reserva=reservaInstance, **pagoData)
        Servicio.objects.create(id_reserva=reservaInstance, **servicioData)

        return personaInstance

    def to_representation(self, obj):
        persona = Persona.objects.get(documento=obj.documento)
        cliente = Cliente.objects.get(documento_persona=obj.documento)
        reserva = Reserva.objects.get(id_cliente=cliente.idCliente)
        plan = Plan.objects.get(id_reserva=reserva.idReserva)
        pago = Pago.objects.get(id_reserva=reserva.idReserva)
        servicio = Servicio.objects.get(id_reserva=reserva.idReserva)

        return{
            'documento': persona.documento,
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'telefono': persona.telefono,
            'email': persona.correo,
            'cliente': {
                'active': cliente.active
            },
            'reserva': {
                'fechaReserva': reserva.fechaReserva,
                'fechaIngreso': reserva.fechaIngreso,
                'fechaSalida': reserva.fechaSalida,
                'costo': reserva.costo

            },
            'plan': {
                'tipoPlan': plan.tipoPlan,
                'precio': plan.precio
            },
            'pago': {
                'tipo_pago': pago.tipo_pago
            },
            'servicio': {
                'nombreServicio': servicio.nombreServicio,
                'descripcion': servicio.descripcion,
                'precioDia': servicio.precioDia
            }



        }
