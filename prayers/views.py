from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import PrayerRequest

class PrayerRequestListView(ListView):
    model = PrayerRequest
    template_name = 'prayers/prayer_list.html'
    context_object_name = 'prayers'
    paginate_by = 10

    def get_queryset(self):
        return PrayerRequest.objects.filter(is_public=True)

class PrayerRequestCreateView(CreateView):
    model = PrayerRequest
    template_name = 'prayers/prayer_submit.html'
    fields = ['name', 'email', 'content', 'is_public']
    success_url = reverse_lazy('prayers:prayer_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            if not form.instance.name:
                form.instance.name = self.request.user.get_full_name() or self.request.user.username
            if not form.instance.email:
                form.instance.email = self.request.user.email
                
        messages.success(self.request, "Your prayer request has been submitted.")
        return super().form_valid(form)
