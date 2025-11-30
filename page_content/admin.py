from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from .models import HeroBanner, ScrollBar, AboutContent

class AdminImagePreviewWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)
        if value and hasattr(value, "url"):
            preview = (
                f'<div style="margin-bottom:8px;">'
                f'<img src="{value.url}" style="max-height:150px;" />'
                f'</div>'
            )
            return mark_safe(preview + input_html)
        return input_html


class ImagePreviewMixin:
    formfield_overrides = {
        models.ImageField: {"widget": AdminImagePreviewWidget},
    }


@admin.register(AboutContent)
class AboutContentAdmin(ImagePreviewMixin, admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AboutContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = AboutContent.objects.first()
        if obj:
            return HttpResponseRedirect(
                reverse(
                    f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                    args=(obj.pk,),
                )
            )
        return super().changelist_view(request, extra_context)


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'preview_image')
    search_fields = ('title',)

    def preview_image(self, obj):
        if obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" width="150" height="80" style="object-fit:cover;" />')
        return "-"
    preview_image.short_description = "Hero Image"


@admin.register(ScrollBar)
class ScrollBarAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)