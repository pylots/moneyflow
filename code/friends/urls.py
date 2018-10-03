from django.conf.urls import url

from .views import friends_list, friends_create, friends_accept
from .consumers import LikeConsumer

app_name = "friends"
urlpatterns = [
    url(r'^list/$', friends_list, name='list'),
    url(r'^create/(?P<pk>\d+)/$', friends_create, name='create'),
    url(r'^accept/(?P<pk>\d+)/$', friends_accept, name='accept'),
]

