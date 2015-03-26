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
	result = RoomAccount.objects.filter(username=user, roomname=roomObj)
	if not result:
		u = RoomAccount(username=user, roomname=roomObj)
		u.save()
	userlObj = RoomAccount.objects.filter(roomname=roomObj)
	userlist = []
	for i in userlObj:
		userlist.append(i.username)
	return render_to_response("chat/room.html", {'user': user, 'roomObj': roomObj, 'userlist': userlist})


def getmsg(request):
	roomid = request.GET.get('roomid')
	roomObj = ChatRoom.objects.get(id=roomid)
	chatpoolObj = ChatPool.objects.filter(roomname=roomObj)
	msglist = []
	for i in chatpoolObj:
		msglist.append(i.msg)
	return HttpResponse(json.dumps(msglist))


def putmsg(request):
	roomid, content = request.POST.get('roomid'), request.POST.get('content')
	roomObj = ChatRoom.objects.get(id=roomid)
	s = ChatPool(roomname=roomObj, msg=content)
	s.save()
	return HttpResponse("OK")


def exituser(request):
	roomid, userid = request.POST.get('roomid'), request.POST.get('userid')
	roomObj = ChatRoom.objects.get(id=roomid)
	userObj = User.objects.get(id=userid)
	u = RoomAccount.objects.filter(username=userObj, roomname=roomObj)
	u.delete()
	return HttpResponse("OK")


def onlineuser(request):
	roomid, userid = request.GET.get('roomid'), request.GET.get('userid')
	roomObj = ChatRoom.objects.get(id=roomid)
	userObj = User.objects.get(id=userid)
	u = RoomAccount.objects.filter(username=userObj, roomname=roomObj)
	if not u:
		u = RoomAccount(username=userObj, roomname=roomObj)
		u.save()
	userlObj = RoomAccount.objects.filter(roomname=roomObj)
	userlist = []
	for i in userlObj:
		userlist.append(str(i.username))
	return HttpResponse(json.dumps(userlist))