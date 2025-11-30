from django.db.models import Count
from rest_framework.decorators import api_view
from .models import (
    CarType, CarBrand, CarBodyType, FuelType, DriveType,
    GearType, OwnerType, Feature, CarModel, ModelYear,
    CarDealer, CarListing, CarImage
)
from .serializers import (
    CarTypeSerializer, CarBrandSerializer, CarBodyTypeSerializer, FuelTypeSerializer,
    DriveTypeSerializer, GearTypeSerializer, OwnerTypeSerializer, FeatureSerializer,
    CarModelSerializer, ModelYearSerializer, CarDealerSerializer,
    CarListingSerializer, CarImageSerializer, CarListingSummarySerializer
)
from isamauto.utils import success_response, error_response


def _list_response(qs, serializer_class, request):
    serializer = serializer_class(qs, many=True, context={'request': request})
    return success_response(serializer.data)


# @api_view(['GET'])
# def get_car_listings(request):
#     qs = CarListing.objects.prefetch_related('features', 'images').all()
#     return _list_response(qs, CarListingSerializer, request)

@api_view(['GET'])
def get_car_listings(request):
    """
    Returns a list of car listings, newest first by default.
    Optional filters via query params:
      - car_type, car_brand, body_type, fuel_type,
        drive_type, gear_type, owner_type, car_model,
        model_year, dealer, status
    e.g. GET /api/car-listings/?car_brand=2&status=On%20Sale
    """
    qs = (
        CarListing.objects
        .prefetch_related('images')
        .annotate(total_images=Count('images'))
        .order_by('-created_at')
    )

    filterable = [
        'car_type', 'car_brand', 'body_type', 'fuel_type',
        'drive_type', 'gear_type', 'owner_type', 'car_model',
        'model_year', 'dealer', 'status'
    ]
    filters = {}
    for param in filterable:
        val = request.query_params.get(param)
        if val is not None and val != '':
            filters[param] = val

    if filters:
        qs = qs.filter(**filters).exclude(status='Pending')

    serializer = CarListingSummarySerializer(
        qs,
        many=True,
        context={'request': request}
    )
    return success_response(serializer.data)


@api_view(['GET'])
def get_car_types(request):
    return _list_response(CarType.objects.all(), CarTypeSerializer, request)


@api_view(['GET'])
def get_car_brands(request):
    qs = CarBrand.objects.annotate(car_count=Count('carlisting'))
    serializer = CarBrandSerializer(qs, many=True, context={'request': request})
    return success_response(serializer.data)


@api_view(['GET'])
def get_car_body_types(request):
    return _list_response(CarBodyType.objects.all(), CarBodyTypeSerializer, request)


@api_view(['GET'])
def get_fuel_types(request):
    return _list_response(FuelType.objects.all(), FuelTypeSerializer, request)


@api_view(['GET'])
def get_drive_types(request):
    return _list_response(DriveType.objects.all(), DriveTypeSerializer, request)


@api_view(['GET'])
def get_gear_types(request):
    return _list_response(GearType.objects.all(), GearTypeSerializer, request)


@api_view(['GET'])
def get_owner_types(request):
    return _list_response(OwnerType.objects.all(), OwnerTypeSerializer, request)


@api_view(['GET'])
def get_features(request):
    return _list_response(Feature.objects.all(), FeatureSerializer, request)


@api_view(['GET'])
def get_car_models(request):
    return _list_response(CarModel.objects.all(), CarModelSerializer, request)


@api_view(['GET'])
def get_model_years(request):
    qs = ModelYear.objects.all().order_by('-year')
    return _list_response(qs, ModelYearSerializer, request)


@api_view(['GET'])
def get_car_dealers(request):
    return _list_response(CarDealer.objects.all(), CarDealerSerializer, request)


@api_view(['GET'])
def get_car_images(request):
    return _list_response(CarImage.objects.all(), CarImageSerializer, request)


@api_view(['GET'])
def get_car_detail(request, slug):
    """
    Lookup a single CarListing by slug and return its full serialized data.
    """
    try:
        car = CarListing.objects.prefetch_related('features', 'images') \
                               .get(slug=slug)
    except CarListing.DoesNotExist:
        return error_response(404, 'Car listing not found.')
    serializer = CarListingSerializer(car, context={'request': request})
    return success_response(serializer.data)