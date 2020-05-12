from django.urls import path

from . import views


app_name = 'chat-app'
urlpatterns = [
    path('', views.ChatPageView.as_view(), name='chat-page'),
    path('<str:room_name>/', views.RoomPageView.as_view(), name='room'),
]
