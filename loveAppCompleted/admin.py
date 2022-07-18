from django.contrib import admin
from .models import loveChatModel

# Register your models here.

@admin.register(loveChatModel)
class loveChatModelAdmin(admin.ModelAdmin):
    list_display = ['id','message','timestamp','user']