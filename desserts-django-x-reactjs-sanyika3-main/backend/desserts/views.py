from django.shortcuts import render
from .models import Dessert,DesertCategory
from rest_framework.decorators import api_view
from rest_framework import response
from . import serializers

# Create your views here.

def indexPage(request):
    return render(request, "index.html")

@api_view(["GET"])
def GetAll(request):
    deserts = models.Desert.objects.all()
    ser = serializers.DessertSerializers(deserts,many=True)
    return response(ser.data,safe=False)
    