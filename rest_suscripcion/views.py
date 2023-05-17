from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Suscriptores
from .serializers import SuscriptoresSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_suscriptores(req):
    if req.method == 'GET':
        suscriptor = Suscriptores.objects.all()
        serializer = SuscriptoresSerializer(suscriptor, many=True)
        return Response (serializer.data)
    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = SuscriptoresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view (['GET', 'PUT', 'DELETE'])
def suscripcion_detalles(req, id):
    try:
        suscriptor = Suscriptores.objects.get(correo=id)
    except Suscriptores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'GET':
        serializer = SuscriptoresSerializer(suscriptor)
        return Response(serializer.data)
    if req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = SuscriptoresSerializer(suscriptor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        suscriptor.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)