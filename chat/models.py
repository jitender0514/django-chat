from django.db import models
from django.conf import settings

# Create your models here.

RoomType = (
    (1, "direct"),
    (2, "group")
)


class RoomDetails(models.Model):
    room = models.CharField(max_length=8,
                            unique=True,
                            null=False,
                            blank=False,
                            verbose_name="Room unique name (Randomly generate)")
    room_name = models.CharField(max_length=50,
                                 blank=False,
                                 null=False)
    room_type = models.IntegerField(choices=RoomType, default=RoomType[0][0])
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    is_active = models.BooleanField(default=True,
                                    verbose_name="Is room Active")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room


# class RoomParticipants(models.Model):
#     participant = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                     on_delete=models.DO_NOTHING,
#                                     related_name="user_rooms",
#                                     )
#     room = models.ForeignKey(RoomDetails,
#                              on_delete=models.DO_NOTHING,
#                              related_name="room_participants",
#                              )
#
#     def __str__(self):
#         return self.room.room_name


class Messages(models.Model):
    content = models.TextField(blank=False,
                               null=False,
                               verbose_name="Content of the message")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.DO_NOTHING,
                              related_name="user_participant",
                              )
    room = models.ForeignKey(RoomDetails,
                             on_delete=models.DO_NOTHING,
                             related_name="room_messages",
                             )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room.room_name


