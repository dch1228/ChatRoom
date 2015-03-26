from django.conf.urls import patterns, url
from chat import views


urlpatterns = patterns(
	'',
	url(r'^$', views.index),
	url(r'^(\d)$', views.room),
	url(r'^getmsg/$', views.getmsg),
	url(r'^putmsg/$', views.putmsg),
	url(r'^exitchat/$', views.exituser),
	url(r'^onlinelist/$', views.onlineuser),
)