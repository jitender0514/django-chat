from django.urls import re_path, include, path
from rest_framework.authtoken import views
from rest_framework import routers
from api import views as api_views

app_name = 'api'


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'room-detail', api_views.RoomDetailViewSet)
router.register(r'message', api_views.MessageViewSet)

urlpatterns = [
    re_path('^(?P<version>(v1))/', include(router.urls)),
    re_path(r'^(?P<version>(v1))/api-token-auth/', views.obtain_auth_token),
    ]
