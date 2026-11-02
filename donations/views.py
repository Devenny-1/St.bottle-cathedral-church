from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Donation

class DonationView(CreateView):
    model = Donation
    template_name = 'donations/donate.html'
    fields = ['name', 'email', 'amount']
    success_url = reverse_lazy('donations:donation_success')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            if not form.instance.name:
                form.instance.name = self.request.user.get_full_name() or self.request.user.username
            if not form.instance.email:
                form.instance.email = self.request.user.email
        form.instance.status = 'completed' # For demo purposes, auto-complete
        return super().form_valid(form)

class DonationSuccessView(TemplateView):
    template_name = 'donations/success.html'
