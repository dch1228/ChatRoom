from django.contrib import admin
from chat.models import ChatRoom, RoomAccount, ChatPool
# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(RoomAccount)
admin.site.register(ChatPool)