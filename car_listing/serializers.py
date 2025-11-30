from rest_framework import serializers
from django.db.models import Count
from .models import (
    CarType, CarBrand, CarBodyType, FuelType, DriveType,
    GearType, OwnerType, Feature, CarModel, ModelYear,
    CarDealer, CarListing, CarImage
)


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ('id', 'name', 'created_at', 'updated_at')


class CarBrandSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    car_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CarBrand
        fields = (
            'id', 'title', 'logo', 'created_at', 'updated_at',
            'logo_url', 'car_count'
        )

    def get_logo_url(self, obj):
        request = self.context.get('request')
        if obj.logo and request:
            return request.build_absolute_uri(obj.logo.url)
        return None


class CarBodyTypeSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CarBodyType
        fields = (
            'id', 'title', 'image', 'created_at', 'updated_at', 'image_url'
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ('id', 'title', 'created_at', 'updated_at')


class DriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveType
        fields = ('id', 'title', 'created_at', 'updated_at')


class GearTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearType
        fields = ('id', 'title', 'created_at', 'updated_at')


class OwnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerType
        fields = ('id', 'title', 'created_at', 'updated_at')


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'title', 'created_at', 'updated_at')


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'title', 'created_at', 'updated_at')


class ModelYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelYear
        fields = ('id', 'year', 'created_at', 'updated_at')


class CarDealerSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CarDealer
        fields = (
            'id', 'name', 'image', 'location', 'location_name', 
            'contact_number', 'whatsapp_link', 'image_url', 'is_verified', 'created_at', 'updated_at',
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class CarImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CarImage
        fields = (
            'id', 'car', 'image', 'alt_text', 'is_featured',
            'image_url'
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class CarListingSerializer(serializers.ModelSerializer):
    car_type = CarTypeSerializer(read_only=True)
    car_brand = CarBrandSerializer(read_only=True)
    body_type = CarBodyTypeSerializer(read_only=True)
    fuel_type = FuelTypeSerializer(read_only=True)
    drive_type = DriveTypeSerializer(read_only=True)
    gear_type = GearTypeSerializer(read_only=True)
    owner_type = OwnerTypeSerializer(read_only=True)
    car_model = CarModelSerializer(read_only=True)
    model_year = ModelYearSerializer(read_only=True)
    dealer = CarDealerSerializer(read_only=True)
    features = FeatureSerializer(many=True, read_only=True)
    images = CarImageSerializer(many=True, read_only=True)
    featured_image = serializers.SerializerMethodField()

    class Meta:
        model = CarListing
        fields = '__all__'

    def get_featured_image(self, obj):
        featured = obj.images.filter(is_featured=True).first()
        if featured:
            return CarImageSerializer(featured, context=self.context).data
        return None


class CarListingSummarySerializer(serializers.ModelSerializer):
    body_type      = CarBodyTypeSerializer(read_only=True)
    fuel_type      = FuelTypeSerializer(read_only=True)
    gear_type      = GearTypeSerializer(read_only=True)
    model_year     = ModelYearSerializer(read_only=True)
    featured_image = serializers.SerializerMethodField()
    total_images   = serializers.IntegerField(read_only=True)

    class Meta:
        model  = CarListing
        fields = [
            'title',
            'slug',
            'body_type',
            'fuel_type',
            'mileage',
            'gear_type',
            'selling_price',
            'status',
            'total_images',
            'featured_image',
            'model_year',
        ]

    def get_featured_image(self, obj):
        img = obj.images.filter(is_featured=True).first()
        return CarImageSerializer(img, context=self.context).data if img else None