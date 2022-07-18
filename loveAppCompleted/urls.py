from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Neha ),
    path('Sonu',views.Sonu),
    path('log',views.Chatlog),
    path('callkangaroo', views.Call),
    path('notifykangaroo', views.notification),
    path('Eva' , views.Eva),
    path('Adam' , views.Adam),

]