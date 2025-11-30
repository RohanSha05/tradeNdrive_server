from rest_framework import serializers
from .models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    favicon = serializers.SerializerMethodField()
    secondary_logo = serializers.SerializerMethodField()

    class Meta:
        model = Settings
        fields = '__all__'

    def get_logo(self, obj):
        request = self.context.get('request')
        if obj.logo and request:
            return request.build_absolute_uri(obj.logo.url)
        return None

    def get_favicon(self, obj):
        request = self.context.get('request')
        if obj.favicon and request:
            return request.build_absolute_uri(obj.favicon.url)
        return None

    def get_secondary_logo(self, obj):
        request = self.context.get('request')
        if obj.secondary_logo and request:
            return request.build_absolute_uri(obj.secondary_logo.url)
        return None
