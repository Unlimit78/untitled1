from django.urls import path
from .views import dialogs,new_chat,chat,delete_chat

urlpatterns = [
    path('accounts/profile/chats/',dialogs,name='chats'),
    path('accounts/profile/chats/new_chat/',new_chat,name='new_chat'),
    path('accounts/profile/chats/<int:chat_pk>/',chat,name='chat'),
    path('accounts/profile/chats/delete/<int:chat_pk>/',delete_chat,name='delete_chat'),
]
