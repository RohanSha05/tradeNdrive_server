from django.urls import path
from .views import get_hero_banners, get_scroll_bars, get_about_content

urlpatterns = [
    path('hero-banners/', get_hero_banners, name='get-hero-banners'),
    path('scroll-bars/', get_scroll_bars, name='get-scroll-bars'),
    path('about-content/', get_about_content, name='get-about-content'),
]
