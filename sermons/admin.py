from django.contrib import admin
from .models import Sermon

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'preacher', 'date_delivered']
    list_filter = ['date_delivered', 'preacher']
    search_fields = ['title', 'preacher', 'description']
