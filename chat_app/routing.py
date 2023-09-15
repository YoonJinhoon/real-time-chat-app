### 웹 소켓 라우팅 설정 파일

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat_rooms import consumers

application = ProtocolTypeRouter({
    # 웹 소켓 라우터 설정
    "websocket": URLRouter(
        [
            path("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
        ]
    ),
})