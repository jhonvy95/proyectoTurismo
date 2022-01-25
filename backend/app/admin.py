from django.contrib import admin

# Register your models here.

from .models.persona import Persona
from .models.cliente import Cliente
from .models.reserva import Reserva
from .models.plan import Plan
from .models.pago import Pago
from .models.servicio import Servicio

admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Plan)
admin.site.register(Pago)
admin.site.register(Servicio)
