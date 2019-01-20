import json

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'chats/index.html'


class Room(LoginRequiredMixin, TemplateView):
    template_name = 'chats/chat.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context.update(
            room_name=self.kwargs.get('room_name'),
            room_name_json=mark_safe(json.dumps(self.kwargs.get('room_name')))
        )
        return context


index = Index.as_view()
room = Room.as_view()
