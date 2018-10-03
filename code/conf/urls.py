from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from profiles.models import Profile
from authtools.models import User

from . import views

urlpatterns = [
    url('^$', views.HomePage.as_view(), name="home"),
    url(r'^about/', views.AboutPage.as_view(), name="about"),
    url(r'^users/', include('profiles.urls')),
    url(r'^xkcd/', admin.site.urls),
    url(r'^friends/', include('friends.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^friendship/', include('friendship.urls')),
    ]

from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

# Serializers define the API representation.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
