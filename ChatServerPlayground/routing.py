from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path


application = ProtocolTypeRouter({
   'websocket': AllowedHostsOriginValidator(
                                              AuthMiddlewareStack(
                                              #URLRouter([....]) #empty  till we have a consumer
                                              )
                                             ),
})
