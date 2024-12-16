from django.shortcuts import get_object_or_404, redirect
from .models import ShortenedLink

def redirect_to_original(request, custom_name):
    link = get_object_or_404(ShortenedLink, custom_name=custom_name)
    return redirect(link.original_url)
