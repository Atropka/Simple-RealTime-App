from django.urls import path
from .consumers import RandomNumber

ws_urlpatterns = [
    path('ws/jokes/', RandomNumber.as_asgi())
]