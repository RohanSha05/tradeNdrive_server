from django.urls import path
from .views import get_settings

urlpatterns = [
    path('', get_settings, name='get_settings'),
]