from drfapp.models import employee
from rest_framework import serializers

class empserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'