from django.contrib import admin
from django.urls import path, include
from .views import server_info, hf_proxy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', server_info),
    path('api/settings/', include('site_setting.urls')),
    path('api/', include('car_listing.urls')),
    path('api/', include('page_content.urls')),
    path('api/', include('loan_application.urls')),
    path('api/hf/<path:model>', hf_proxy),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )