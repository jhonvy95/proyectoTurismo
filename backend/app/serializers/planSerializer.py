from django.db.models import fields
from app.models.plan import Plan
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['tipoPlan', 'precio']
