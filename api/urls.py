from django.urls import re_path
from rest_framework.authtoken import views

app_name = 'api'
urlpatterns = [
    re_path(r'^(?P<version>(v1))/api-token-auth/', views.obtain_auth_token)
]