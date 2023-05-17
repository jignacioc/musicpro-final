from dataclasses import fields
from rest_framework import serializers
from core.models import Suscriptores

class SuscriptoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscriptores
        fields = ['correo', 'id_suscripcion', 'estado']