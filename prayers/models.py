from django.db import models
from django.conf import settings

class PrayerRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    content = models.TextField()
    is_public = models.BooleanField(default=False, help_text="Can this be shared with the congregation?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prayer from {self.name} on {self.created_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-created_at']
