from django.contrib import admin
from .models import ShortenedLink

@admin.register(ShortenedLink)
class ShortenedLinkAdmin(admin.ModelAdmin):
    list_display = ('custom_name', 'original_url', 'created_at')
    search_fields = ('custom_name', 'original_url')
