"""
ASGI config for Neha project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

# from email.mime import application
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Neha.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import loveAppCompleted.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Neha.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                loveAppCompleted.routing.ws_application
            )
        )
    )
})
