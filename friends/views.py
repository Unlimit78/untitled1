from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required

from .models import Friend
from main.models import AdvUser
from .forms import FindFriendForm
from main.models import Photos

def other_profiles(request,other_id):
    other = AdvUser.objects.get(pk=other_id)
    photos = Photos.objects.filter(location=other)
    friends = Friend.objects.filter(from_user=request.user)
    context = {'other':other,'friends':friends,'photos':photos}
    return render(request,'friends/other_profiles.html',context)

@login_required
def find_friend(request):
    form = FindFriendForm()
    users = AdvUser.objects.all()
    context = {'form':form,'users':users}
    if request.method=='POST':
        form = FindFriendForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['find']
            friend = AdvUser.objects.get(username=data)
            context = {'form':form,'users':users,'friend':friend}
            return render(request,'friends/find_friend.html',context)
    else:
        return render(request,'friends/find_friend.html',context)

@login_required
def add_friend(request,friend_id):
    one = AdvUser.objects.get(pk=friend_id)
    second = AdvUser.objects.get(pk=request.user.pk)
    if one!=second :
        friend_ship = Friend.objects.get_or_create(to_user=one,from_user=second)
    return HttpResponseRedirect(reverse('find_friend'))

@login_required
def delete_friend(request,friend_id):
    one = Friend.objects.get(pk=friend_id)
    one.delete()
    return HttpResponseRedirect(reverse('friends'))

@login_required
def friends(request):
    users = AdvUser.objects.all()
    friends = Friend.objects.filter(from_user=request.user)
    context = {'friends':friends,'users':users}
    return render(request,'friends/self_friends.html',context)
