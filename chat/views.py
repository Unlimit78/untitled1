from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required
from .models import Dialog,Message
from friends.models import Friend

from .forms import MessageForm



@login_required
def dialogs(request):
    chats = Dialog.objects.filter(members__in=[request.user])
    messages = Message.objects.filter(is_readed=False)
    context = {'chats': chats,'messages':messages}
    return render(request,'chat/chats.html',context)

@login_required
def new_chat(request):
    friends = Friend.objects.filter(from_user=request.user)
    dialog = Dialog.objects.create()
    context = {'friends':friends,'chat':dialog}
    return render(request,'chat/new_chat.html',context)

@login_required
def chat(request,chat_pk):
    dialog = Dialog.objects.get(pk=chat_pk)
    chats = Dialog.objects.filter(members__in=[request.user])
    form = MessageForm()
    messages = Message.objects.filter(chat=dialog)
    context = {'form':form,
               'messages':messages,
               'chats':chats,
               }
    return render(request,'chat/chat.html',context)

@login_required
def delete_chat(request,chat_pk):
    chat = Dialog.objects.get(pk=chat_pk)
    chat.delete()
    return HttpResponseRedirect(reverse('chats'))
