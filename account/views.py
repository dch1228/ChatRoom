# coding: utf-8

from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext


def login(request):
	# 用于保存登录状态
	data = {'loginStatus': ''}
	# 判断请求方法
	if request.method == 'POST':
		# 获取用户名和密码
		username = request.POST.get('username')
		password = request.POST.get('password')
		# 认证用户,如果账号密码匹配则返回用户名,否则返回None
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			# 登录用户
			auth.login(request, user)
			return HttpResponseRedirect('/chat')
		# 如果账号密码不匹配返回的信息
		data['loginStatus'] = u'用户名或密码错误!'
	return render_to_response('account/login.html', data, context_instance=RequestContext(request))


@login_required(login_url='/account/login')
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/account/login')