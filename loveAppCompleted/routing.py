from django.urls import path, re_path
from loveAppCompleted.consumers import loveChat , loveNotification, ChatConsumer

ws_application = [
    path('ws/loveChat/',loveChat.as_asgi()),
    path('ws/Notification/',loveNotification.as_asgi()),
    re_path(r'', ChatConsumer.as_asgi()),
]