from django.contrib import admin
from .models import PrayerRequest

@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_public']
    list_filter = ['is_public', 'created_at']
    search_fields = ['name', 'content']
