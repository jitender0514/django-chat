from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class ChatPageView(TemplateView):

    template_name = "chat/chat.html"


class RoomPageView(TemplateView):

    template_name = "chat/room.html"

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['room_name'] = kwargs['room_name']
        return context
