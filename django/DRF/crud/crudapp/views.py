from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudapp.models import employeee
from crudapp.serializers import serialEmp
# Create your views here.

@api_view(['POST'])
def createemp(req):
    emp_serializer=serialEmp(data=req.data)
    if emp_serializer.is_valid():
        emp_serializer.save()
    return Response(emp_serializer.data)

@api_view(['POST'])
def updateemp(req,id):
    updateval=employeee.objects.get(id=id)
    emp_serializer=serialEmp(instance=updateval,data=req.data)
    if emp_serializer.is_valid():
        emp_serializer.save()
    return Response(emp_serializer.data)

@api_view(['GET'])
def reademp(req):
    emp_data=employeee.objects.all()
    print(type(emp_data))
    emp_serializer=serialEmp(emp_data, many=True)
    return Response({'Employee_data':emp_serializer.data})

@api_view(['DELETE'])
def deleteemp(req,id):
    deleteval=employeee.objects.get(id=id)
    deleteval.delete()
    return Response("Deleted successsfully")