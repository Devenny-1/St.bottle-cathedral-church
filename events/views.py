from django.views.generic import ListView, DetailView
from .models import Event
from django.utils import timezone

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
