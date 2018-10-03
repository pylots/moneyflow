import logging

from uuid import UUID, uuid4

from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateContractForm, UpdateContractForm

from authtools.models import User
from friendship.models import Friend, Follow, Block, FriendshipRequest
from friendship.signals import friendship_request_created
from django.dispatch import receiver

log = logging.getLogger(__name__)

@login_required
def friends_list(request):
    
    friends = Friend.objects.friends(request.user)
    candidates = User.objects.exclude(friends__from_user=request.user).exclude(id=request.user.id)
    requests = Friend.objects.unrejected_requests(user=request.user)
    groups = request.user.groups.all()
    
    return render(
        request,
        "friends/list.html",
        {'friends': friends, 'candidates': candidates, 'requests': requests, 'groups': groups, 'user': request.user},
    )


@login_required
def friends_accept(request, pk):
    friend_request = FriendshipRequest.objects.get(pk=pk)
    friend_request.accept()
    return HttpResponseRedirect(reverse("friends:list"))

@login_required
def friends_create(request, pk):
    friend = User.objects.get(pk=pk)
    Friend.objects.add_friend(
        request.user,
        friend,
        message="Hi! I would like to add tou")
    return HttpResponseRedirect(reverse("friends:list"))


@receiver(friendship_request_created)
def request_created(sender, **kwargs):
    print("request:", sender, kwargs)
    
