from rest_framework import serializers
from crudapp.models import employeee

class serialEmp(serializers.ModelSerializer):
    class Meta:
        model=employeee
        fields='__all__'