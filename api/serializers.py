from django.contrib.auth.models import User, Group
from rest_framework import serializers
from chat.models import RoomDetails, Messages


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")  # define namespace

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class RoomDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomDetails
        fields = ['room', 'room_name', 'is_active', 'created']


class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = ['content', 'owner', 'participants', 'room', 'created']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['name']
