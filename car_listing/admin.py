from django.contrib import admin
from django.utils.html import format_html

from .models import (
    CarType, CarBrand, CarBodyType, FuelType, DriveType, GearType,
    OwnerType, Feature, CarModel, ModelYear, CarDealer,
    CarListing, CarImage
)

# ─── Custom Dashboard (optional) ────────────────────────────────────────────────
original_index = admin.site.index
def custom_index(request, extra_context=None):
    data = [
        {"name": "Total Listings",   "count": CarListing.objects.count()},
        {"name": "Total Brands",     "count": CarBrand.objects.count()},
        {"name": "Total Dealers",    "count": CarDealer.objects.count()},
        {"name": "Total Car Types",  "count": CarType.objects.count()},
        {"name": "Total Models",     "count": CarModel.objects.count()},
        {"name": "Total Body Types", "count": CarBodyType.objects.count()},
    ]
    extra_context = extra_context or {}
    extra_context['custom_dashboard'] = data
    return original_index(request, extra_context)

admin.site.index = custom_index


# ─── CarImage Inline (single-file upload + preview) ────────────────────────────
class CarImageInline(admin.StackedInline):
    model = CarImage
    fk_name = 'car'
    extra = 1
    fields = ('image', 'alt_text', 'is_featured', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" width="150" style="object-fit:contain; border:1px solid #ddd;"/>',
                obj.image.url
            )
        return ""
    image_preview.short_description = 'Preview'


# ─── CarListing Admin ──────────────────────────────────────────────────────────
@admin.register(CarListing)
class CarListingAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]

    list_display = (
        'title', 'car_brand', 'model_year',
        'selling_price', 'status', 'dealer', 'featured_thumbnail'
    )
    list_filter = ('status', 'car_brand', 'model_year')
    search_fields = ('title', 'stock_number', 'vin_number')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        ('Basic Info',      {'fields': ('title', 'slug', 'status', 'video_url', 'carfax')}),
        ('Specs & Dealer',  {'fields': (
            'car_type','car_brand','body_type','fuel_type',
            'drive_type','gear_type','owner_type',
            'car_model','model_year','dealer'
        )}),
        ('Pricing & Stock', {'fields': (
            'selling_price','mileage','monthly_installment_price',
            'installment_month','stock_number','vin_number'
        )}),
        ('Vehicle Details', {'fields': (
            'doors','seats','engine_size','cylinders',
            ('interior_colors','exterior_colors'),
        )}),
        ('Descriptions',    {'fields': (
            'description','comfort_convenience',
            'interior_description','exterior_description',
            'safety','entertainment_communication','features'
        )}),
    ]

    def featured_thumbnail(self, obj):
        featured = obj.images.filter(is_featured=True).first()
        if featured:
            return format_html('<img src="{}" width="50"/>', featured.image.url)
        return '-'
    featured_thumbnail.short_description = 'Featured'


# ─── Other Models ─────────────────────────────────────────────────────────────
@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')
    search_fields  = ('name',)

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display    = ('title','logo_preview','created_at')
    readonly_fields = ('logo_preview',)
    search_fields   = ('title',)
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100"/>', obj.logo.url)
        return ""
    logo_preview.short_description = 'Logo'

@admin.register(CarBodyType)
class CarBodyTypeAdmin(admin.ModelAdmin):
    list_display    = ('title','image_preview','created_at')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100"/>', obj.image.url)
        return ""
    image_preview.short_description = 'Image'

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display  = ('title','created_at')
    search_fields = ('title',)

@admin.register(DriveType)
class DriveTypeAdmin(admin.ModelAdmin):
    list_display  = ('title','created_at')
    search_fields = ('title',)

@admin.register(GearType)
class GearTypeAdmin(admin.ModelAdmin):
    list_display  = ('title','created_at')
    search_fields = ('title',)

@admin.register(OwnerType)
class OwnerTypeAdmin(admin.ModelAdmin):
    list_display  = ('title','created_at')
    search_fields = ('title',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display  = ('title','created_at')
    search_fields = ('title',)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display  = ('title','created_at')
    search_fields = ('title',)

@admin.register(ModelYear)
class ModelYearAdmin(admin.ModelAdmin):
    list_display  = ('year','created_at')
    search_fields = ('year',)

@admin.register(CarDealer)
class CarDealerAdmin(admin.ModelAdmin):
    list_display    = ('name','location_name','contact_number','is_verified','created_at')
    list_filter     = ('is_verified',)
    readonly_fields = ('image_preview',)
    search_fields   = ('name','location_name','contact_number')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100"/>', obj.image.url)
        return ""
    image_preview.short_description = 'Logo'
