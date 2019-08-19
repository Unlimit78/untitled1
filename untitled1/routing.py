from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat.consumers import ChatSocket,DialogSocket

application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('c/accounts/profile/chats/<int:chat_pk>/',ChatSocket),
                path('c/accounts/profile/chats/new_chat/',DialogSocket),

            ])
        )
    )
})
