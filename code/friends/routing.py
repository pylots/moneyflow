from django.conf.urls import url

from .consumers import LikeConsumer

websocket_urlpatterns = [
    url(r'^ws/like/(?P<userid>\d+)/$', LikeConsumer),
]
