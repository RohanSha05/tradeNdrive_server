from rest_framework.decorators import api_view
from .models import Settings
from .serializers import SettingsSerializer
from isamauto.utils import success_response, error_response

@api_view(['GET'])
def get_settings(request):
    settings = Settings.objects.first()
    if not settings:
        return error_response(404, "Site settings have not been configured yet.")
    serializer = SettingsSerializer(settings, context={'request': request})
    return success_response(serializer.data)