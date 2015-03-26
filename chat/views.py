from django.shortcuts import render_to_response, HttpResponse
from chat.models import ChatRoom, RoomAccount, ChatPool
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


@login_required(login_url='/account/login')
def index(request):
	user = request.user
	RoomObj = ChatRoom.objects.all()
	return render_to_response("chat/index.html", {'user': user, 'RoomObj': RoomObj})


@login_required(login_url='/account/login')
def room(request, roomid):
	user = request.user
	roomObj = ChatRoom.objects.get(id=roomid)
	result = RoomAccount.objects.filter(username=user,roomname=roomObj)
	if not result:
		u = RoomAccount(username=user,roomname=roomObj)
		u.save()
	userlObj = RoomAccount.objects.filter(roomname=roomObj)
	userlist = []
	for i in userlObj:
		userlist.append(i.username)
	return render_to_response("chat/room.html", {'user': user, 'roomObj': roomObj, 'userlist':userlist})


@login_required(login_url='/account/login')
def getmsg(request):
	roomid = request.GET.get('roomid')
	roomObj = ChatRoom.objects.get(id=roomid)
	chatpoolObj = ChatPool.objects.filter(roomname=roomObj)
	msglist = []
	for i in chatpoolObj:
		msglist.append(i.msg)
	return HttpResponse(json.dumps(msglist))


@login_required(login_url='/account/login')
def putmsg(request):
	roomid, content = request.POST.get('roomid'), request.POST.get('content')
	roomObj = ChatRoom.objects.get(id=roomid)
	s = ChatPool(roomname=roomObj, msg=content)
	s.save()
	print ChatPool.objects.all()
	return HttpResponse("OK")