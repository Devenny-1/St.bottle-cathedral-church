from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactMessage
from events.models import Event
from sermons.models import Sermon

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_sermons'] = Sermon.objects.all()[:3]
        context['upcoming_events'] = Event.objects.all()[:3]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class LivestreamView(TemplateView):
    template_name = 'core/livestream.html'

class ContactView(CreateView):
    model = ContactMessage
    template_name = 'core/contact.html'
    fields = ['name', 'email', 'subject', 'message']
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        messages.success(self.request, "Thank you for contacting us. We will get back to you soon.")
        return super().form_valid(form)
