from django.conf.urls import patterns, url
from account import views


urlpatterns = patterns(
	'',
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
)