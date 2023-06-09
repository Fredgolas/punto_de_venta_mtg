from rest_framework import serializers
from productos.models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('pk', 'name', 'price', 'quantity', 'types', 'set', 'collector_number', 'condition', 'finish')
