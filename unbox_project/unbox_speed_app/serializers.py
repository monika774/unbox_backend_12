from rest_framework import serializers
from .models import SpeedData

class SpeedDataSerializer(serializers.ModelSerializer):
    """" 
    This serializer for converting complex data into python datatype 
    """
    class Meta:
        model = SpeedData
        fields = ['id', 'speed', 'timestamp']
