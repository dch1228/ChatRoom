from django.conf.urls import patterns, include, url
from django.contrib import admin
from chat.views import index


urlpatterns = patterns(
	'',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^account/', include('account.urls')),
	url(r'^chat/', include('chat.urls')),
	url(r'^$', index),
)
