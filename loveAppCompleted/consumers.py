from channels.generic.websocket import AsyncJsonWebsocketConsumer, WebsocketConsumer ,AsyncWebsocketConsumer
from .models import loveChatModel
from channels.db import database_sync_to_async 
from asgiref.sync import async_to_sync
import json



class loveChat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content):
        data = content
        if data['command'] == 'join':
            await self.channel_layer.group_add(
                data['groupname'],
                self.channel_name
            )
            print('user added')
        elif data['command'] == 'send':
            if self.scope['user'].is_authenticated:
                await self.channel_layer.group_send(
                    'loveBirds',
                    {
                        'type' : 'loveChat.message',
                        'message' : data['message'],
                        'user' : str(self.scope['user'])
                    }
                )
                chat = loveChatModel(
                    message = data['message'],
                    user = str(self.scope['user'])
                )
                await database_sync_to_async(chat.save)()
            else:
                await self.send_json({
                        'warning' : True
                })
    async def loveChat_message(self, event):
        await self.send_json({
            'message' : event['message'],
            'user' : event['user']
        })
    async def disconnect(self,event):
        print('disconnected',event)


class loveNotification(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.room_name = 'loveNotification_room'
        self.room_group_name = 'loveNotification'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.send(text_data= json.dumps({
            'status':'connected from djagno channels'
        }))

    def receive(self, text_data):
        print(text_data)
        

    def disconnect(self,*args, **kwargs):
        print('disconnected')

    def send_notification(self, event):
        print('event is ...', event)
        self.send(text_data = json.dumps({
            'status' : event['value']
        }))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name ='Test-Room'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print('Disconnected!')

    async def receive(self, text_data):
        receive_dict = json.loads(text_data)
        message = receive_dict['message']
        action = receive_dict['action']

        if (action == 'new-offer') or (action == 'new-answer'):
            receiver_channel_name = receive_dict['message']['receiver_channel_name']

            receive_dict['message']['receiver_channel_name'] = self.channel_name
            
            await self.channel_layer.send(
                receiver_channel_name,
                {
                    'type': 'send.sdp',
                    'receive_dict': receive_dict
                }
            )        


            return

        receive_dict['message']['receiver_channel_name'] = self.channel_name

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send.sdp',
                'receive_dict': receive_dict
            }
        )

    async def send_sdp(self, event):
        receive_dict = event['receive_dict']

        await  self.send(text_data=json.dumps(receive_dict))