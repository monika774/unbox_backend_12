import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from asgiref.sync import sync_to_async
from .models import SpeedData


class Speedometer(AsyncWebsocketConsumer):
    #Calling when websocket connection establish
    async def connect(self):
        await self.channel_layer.group_add("speedometer_group", self.channel_name)
        await self.accept()
    
    
    #Calling when web socked connection disconnet 
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("speedometer_group", self.channel_name)


    # A synchronous method wrapped with @sync_to_async to save speed data to the database
    @sync_to_async
    def save_speed_data(self, speed):
        return SpeedData.objects.create(speed=speed)
    

    #Called when websocker receiving message
    async def receive(self, text_data):
        data = json.loads(text_data)
        speed = data.get('speed', 0)
        speed_instance = await self.save_speed_data(speed)
        await self.channel_layer.group_send(
            "speedometer_group",
            {
                "type": "speed_update",
                "speed": speed,
                "timestamp": str(speed_instance.timestamp)
            }
        )
    # processing "speed update" event  
    async def speed_update(self, event):
        await self.send(text_data=json.dumps({
            'speed': event['speed'],
            'timestamp': event['timestamp']
        }))