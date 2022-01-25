from rest_framework import generics, status
from rest_framework import generics, status
from rest_framework.response import Response

from app.models.persona import Persona
from app.serializers.personaSerializer import PersonaSerializer


class PersonaDetailView(generics.RetrieveAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
