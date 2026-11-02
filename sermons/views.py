from django.views.generic import ListView, DetailView
from .models import Sermon

class SermonListView(ListView):
    model = Sermon
    template_name = 'sermons/sermon_list.html'
    context_object_name = 'sermons'
    paginate_by = 10

class SermonDetailView(DetailView):
    model = Sermon
    template_name = 'sermons/sermon_detail.html'
    context_object_name = 'sermon'
