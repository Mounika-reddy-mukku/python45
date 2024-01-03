from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drfapp.models import employee
from drfapp.serializers import empserializer
# Create your views here.
@api_view(['GET'])
def home(request):
    emp_data=employee.objects.all()
    print(type(emp_data))
    emp_serial=empserializer(emp_data,many=True)
    print(type(emp_serial))
    return Response({'name':"Mounika",'avail':True, 'employees':emp_serial.data})

