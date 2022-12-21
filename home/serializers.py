from rest_framework import serializers
from . import models

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Art
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields='__all__'

class ArtOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ArtOrder
        fields='__all__'
    
    def create(self, validated_data):
        return super().create(validated_data)