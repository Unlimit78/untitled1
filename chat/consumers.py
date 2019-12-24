import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import Message,Dialog
from main.models import AdvUser

class ChatSocket(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_pk']
        self.room = 'chats'+str(self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data=None, bytes_data=None):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author = text_data_json['author']
        chat_pk = self.room_name
        async_to_sync(self.channel_layer.group_send)(
            self.room,
            {
                'type': 'chat_message',
                'message': message,
                'author':author,

            }
        )

        user = AdvUser.objects.get(username=author)
        dialog = Dialog.objects.get(pk=chat_pk)
        message_data = Message.objects.create(message=message, author=user, chat=dialog)
        message_data.save()
        for i in dialog.members.all():
            if i!=user:
                not_readed = Message.objects.filter(chat=dialog,is_readed=False,author=i)
                not_readed.update(is_readed=True)

    def chat_message(self, event):
        message = event['message']
        author = event['author']
        async_to_sync(self.send(text_data=json.dumps({
            'message': message,
            'author':author,


        })))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room,
            self.channel_name
        )

class DialogSocket(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        friend_name = text_data_json['friend_name']
        user = text_data_json['user']
        chat_pk = text_data_json['chat_pk']

        friend = AdvUser.objects.get(username=friend_name)
        user = AdvUser.objects.get(username=user)
        dialog =Dialog.objects.get(pk=chat_pk)
        dialog.members.add(friend)
        dialog.members.add(user)
        print(dialog.members)

    def disconnect(self, code):
        print('closed...')
