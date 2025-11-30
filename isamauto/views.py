import django
import platform
import rest_framework
from rest_framework.decorators import api_view

from .utils import success_response, error_response

@api_view(['GET'])
def server_info(request):
    """
    Return basic info about this API, using the standard response envelope.
    """
    try:
        info = {
            "title": "Isam Auto Backend",
            "django_version": django.get_version(),
            "drf_version": rest_framework.__version__,
            "python_version": platform.python_version(),
        }
        return success_response(info)
    except Exception as exc:
        return error_response(
            code=500,
            message=f"Failed to gather server info: {exc}",
            http_status=500
        )