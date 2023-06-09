from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from productos.models import Card
from productos.serializers import CardSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser

from django.shortcuts import render
from django.urls import reverse_lazy

def home(request):
    #tmpl_vars = {'form': CardForm()}
    return HttpResponse("Aquí pones el index")

@api_view(['GET', 'POST'])
def card_collection(request):
    if request.method == 'GET':
        #Show all cards
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Add card
        data = request.data
        serializer = CardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@parser_classes([JSONParser])
def cart_checkup(request):
    if request.method == 'POST':
        data = request.data
        for row in data:
            card = Card.objects.get(pk=row['pk'])
            if card.is_valid():
                card.quantity -= 1
                card.save()