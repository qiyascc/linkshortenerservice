from django.db import models

class ShortenedLink(models.Model):
    custom_name = models.CharField(max_length=50, unique=True, verbose_name="Kısa Ad")
    original_url = models.URLField(verbose_name="Orijinal URL")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.custom_name
