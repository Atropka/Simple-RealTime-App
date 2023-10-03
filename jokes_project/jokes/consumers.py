from channels.generic.websocket import AsyncWebsocketConsumer


class RandomNumber(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('random_number', self.channel_name)  # Обновляем имя группы
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('random_number', self.channel_name)  # Обновляем имя группы

    async def send_jokes(self, event):
        text_message = str(event['text'])
        await self.send(text_message)
