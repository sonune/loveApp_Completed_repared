from django.contrib import admin
#from .models import loveChatModel
from .models import loveChatModel, oldChats1, oldChats2, oldChats3

# Register your models here.

@admin.register(loveChatModel)
class loveChatModelAdmin(admin.ModelAdmin):
    list_display = ['id','message','timestamp','user']
    
@admin.register(oldChats1)
class oldChats1Admin(admin.ModelAdmin):
    list_display = ['id','message','timestamp','user']


@admin.register(oldChats2)
class oldChats2Admin(admin.ModelAdmin):
    list_display = ['id','message','timestamp','user']


@admin.register(oldChats3)
class oldChats3Admin(admin.ModelAdmin):
    list_display = ['id','message','timestamp','user']
