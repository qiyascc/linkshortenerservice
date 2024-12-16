from django.urls import path
from .views import redirect_to_original

urlpatterns = [
    path('<str:custom_name>/', redirect_to_original, name='redirect'),
]
