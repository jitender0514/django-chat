from django.contrib.auth.models import User, Group
from rest_framework import serializers
from chat.models import RoomDetails, Messages
import uuid


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")  # define namespace

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'is_superuser', "is_active", "password"]
        extra_kwargs = {'password': {'write_only': True},
                        'is_superuser': {'read_only': True},
                        "is_active": {'read_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoomDetailsSerializer(serializers.ModelSerializer):
    room_participants = UserSerializer(many=True, read_only=True, source='participants')

    class Meta:
        model = RoomDetails
        fields = ['room', 'room_name','room_participants', 'participants', 'is_active', 'created']
        extra_kwargs = {'room': {'read_only': True},
                        "is_active": {'read_only': True},
                        "created": {'read_only': True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context', None)
        if context:
            request = kwargs['context']['request']
            if request.method in ['POST']:
                self.fields['room'].required = False

    def generate_random_room_id (self):
        """ Method generate the unique room id and return it."""

        room_id = uuid.uuid4().hex[:8]
        if RoomDetails.objects.filter(room=room_id).exists():
            self.generate_random_room_id()  # if room id already exist then call regenerate room id
        return room_id

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        room = self.generate_random_room_id()
        data = validated_data
        data['room'] = room
        room_details = RoomDetails.objects.create(**data)
        room_details.participants.add(*participants)
        return room_details

    def validate_participants(self, values):
        """
            Validate the participants field.
            Can't create a room with superuser.
        """
        for user in values:
            if user.is_superuser is True:
                raise serializers.ValidationError("Can't add superuser")
        return values


class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = ['content', 'owner', 'room', 'created']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['name']
