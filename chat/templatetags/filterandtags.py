from django import template
from chat.models import Message
from friends.models import Friend
register = template.Library()

@register.simple_tag
def get_users_pk(user,chat):
    for u in chat.members.all():
        if u!=user:
            return u
    return None

@register.simple_tag
def count_messages(chat,user):
    for i in chat.members.all():
        if i!=user:
            messages = Message.objects.filter(author=i,is_readed=False,chat=chat)
            k = messages.count()
            return k

@register.simple_tag
def get_friend(user,friend):
    try:
        if Friend.objects.get(to_user=friend,from_user=user):
            return True
    except:
        return False
    return False