from rest_framework import status, views
from rest_framework.response import Response

from app.models.persona import Persona
from app.serializers.personaSerializer import PersonaSerializer


class PersonaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PersonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transaccion exitosa", status=status.HTTP_201_CREATED)
