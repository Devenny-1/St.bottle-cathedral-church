from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'currency', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'currency']
    search_fields = ['name', 'email', 'payment_intent_id']
