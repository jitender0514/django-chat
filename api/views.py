from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import (UserSerializer,
                             GroupSerializer,
                             RoomDetailsSerializer,
                             MessagesSerializer)
from chat.models import Messages, RoomDetails


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RoomDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows room-detail to be viewed or edited.
    """
    queryset = RoomDetails.objects.all()
    serializer_class = RoomDetailsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows message to be viewed or edited.
    """
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
