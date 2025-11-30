from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from .models import Settings

class AdminImagePreviewWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)
        if value and hasattr(value, "url"):
            preview = (
                f'<div style="margin-bottom:8px;">'
                f'  <img src="{value.url}" style="max-height:150px;"/>'
                f'</div>'
            )
            return mark_safe(preview + input_html)
        return input_html

class ImagePreviewMixin:
    formfield_overrides = {
        models.ImageField: {"widget": AdminImagePreviewWidget},
    }

@admin.register(Settings)
class SettingsAdmin(ImagePreviewMixin, admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Settings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = Settings.objects.first()
        if obj:
            return HttpResponseRedirect(
                reverse(
                    f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                    args=(obj.pk,),
                )
            )
        return super().changelist_view(request, extra_context)
