from datetime import datetime
import time, asyncio
import random
from django.shortcuts import render
from rest_framework import viewsets
from .models import SpeedData
from rest_framework.response import Response
from .serializers import SpeedDataSerializer
from rest_framework import status


class SpeedDataViewSet(viewsets.ModelViewSet):
    queryset = SpeedData.objects.all()
    serializer_class = SpeedDataSerializer
    
    def get_data(self, request):
        """
            This function uses for retriving data
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    
    
    def create_data(self, request):
        """
        This function used for generating data
        """
        if hasattr(request, 'data'):
            serializer = self.get_serializer(data=request.data)
        else:
            serializer = self.get_serializer(data = request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
   
    def create_data_at_intervals(self,request):
        """
        This function showing speed at interval using random speed and current time 
        """
        while True:
            new_obj = {}
            new_obj['speed'] = random.randint(1, 100)
            new_obj['timestamp'] = datetime.now()
            self.create_data(new_obj)
            print(new_obj)
            time.sleep(1)
            


    
        
    
