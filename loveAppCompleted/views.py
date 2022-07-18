from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from requests import request
from .models import loveChatModel, Notification

# Create your views here.

def Neha(request):
    chats = []
    username = 'Eva'
    password = 'sonuwedsneha'
    if username and password:
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            chats = loveChatModel.objects.all()
            min_requrement = (len(chats))
            a = (len(chats) - 5)
            if min_requrement>=6:
                chats = loveChatModel.objects.values('id','timestamp','message','user').order_by('timestamp')[a:]
            else:
                chats = loveChatModel.objects.all()
            return render(request, 'chatApplication.html',{'chats' : chats})
    return render(request, 'chatApplication.html')

def Sonu(request):
    username = 'Adam'
    password = 'sonuwedsneha'
    if username and password:
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            chats = loveChatModel.objects.all()
            min_requrement = (len(chats))
            a = (len(chats) - 5)
            if min_requrement>=6:
                chats = loveChatModel.objects.values('id','timestamp','message','user').order_by('timestamp')[a:]
            else:
                chats = loveChatModel.objects.all()
            return render(request, 'chatApplication.html',{'chats' : chats})
    return render(request, 'chatApplication.html')

def Chatlog(request):
    chats = loveChatModel.objects.all()
    return render(request, 'log.html',{'chats' : chats})
# def Try(request):
#     return render(request, 'try.html')

def Call(request):
    if request.method == "POST":
        # user = request.POST.get('user')
        notification = request.POST.get('noti')
        called = Notification( notification = notification)
        called.regiser()
    return render(request , 'callkangaroo.html')

def notification(request):
    username = 'Adam'
    password = 'sonuwedsneha'
    if username and password:
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return render(request , 'notification.html')
    return render(request , 'notification.html')

def Eva(request):
    context = {
        'user' : 'Eva'
    }
    return render(request, 'videocall.html', context=context)



def Adam(request):
    context = {
        'user' : 'Adam'
    }
    return render(request, 'videocall.html', context=context)
