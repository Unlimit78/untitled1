from django import forms
from .models import FindFriend,Friend


class FindFriendForm(forms.ModelForm):
    class Meta:
        model=FindFriend
        fields = ('find',)

class AddFriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields=[]