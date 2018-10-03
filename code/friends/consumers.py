# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class LikeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['userid']
        self.likes = 'likes'

        await self.channel_layer.group_add(
            self.likes,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.likes,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        userid = text_data_json['like']

        # Send message to room group
        await self.channel_layer.group_send(
            self.likes,
            {
                'type': 'like',
                'like': userid
            }
        )

    # Receive message from room group
    async def like(self, event):
        userid = event['like']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'userid': userid
        }))
        
