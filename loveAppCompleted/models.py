from django.db import models 
from time import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.


class loveChatModel(models.Model):
    # days_left = models.CharField()
    message = models.CharField(max_length=10000, default="")
    timestamp = models.DateTimeField(auto_now = True, null=True, blank = True)
    user = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.user 

channel_layer = get_channel_layer()

class Notification(models.Model):
    # user = models.ForeignKey(User ,on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now = True, null=True, blank = True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.notification
    

    def save(self,*args, **kwargs):
        
        notification_objs = Notification.objects.filter(is_seen = False).count()
        data = { 'count' : notification_objs, 'current_notification':self.notification}
        async_to_sync(channel_layer.group_send)(
            'loveNotification' , {
                'type' : 'send.notification',
                'value' : "Sonu aao"
            }
        )

    def regiser(self):
        self.save()
    