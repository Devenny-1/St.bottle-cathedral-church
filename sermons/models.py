from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    date_delivered = models.DateField()
    preacher = models.CharField(max_length=100)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube or Vimeo URL")
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='sermons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_delivered']
