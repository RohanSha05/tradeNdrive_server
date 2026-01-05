from django.db.models import Count, Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    CarType, CarBrand, CarBodyType, FuelType, DriveType,
    GearType, OwnerType, Feature, CarModel, ModelYear,
    CarDealer, CarListing, CarImage, CarReview
)
from .serializers import (
    CarTypeSerializer, CarBrandSerializer, CarBodyTypeSerializer, FuelTypeSerializer,
    DriveTypeSerializer, GearTypeSerializer, OwnerTypeSerializer, FeatureSerializer,
    CarModelSerializer, ModelYearSerializer, CarDealerSerializer,
    CarListingSerializer, CarImageSerializer, CarListingSummarySerializer, CarReviewSerializer
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


@api_view(['POST'])
def submit_car_review(request):
    """
    Submit a review for a car listing.
    
    Required fields:
    - car_id: int
    - rating: int (1-5)
    - comment: str
    - user_email: str
    - user_name: str
    """
    try:
        car_id = request.data.get('car_id')
        rating = request.data.get('rating')
        comment = request.data.get('comment')
        user_email = request.data.get('user_email')
        user_name = request.data.get('user_name')

        # Validate required fields
        if not all([car_id, rating, comment, user_email, user_name]):
            return error_response(
                400,
                'Missing required fields: car_id, rating, comment, user_email, user_name',
                400
            )

        # Validate rating is between 1 and 5
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                return error_response(400, 'Rating must be between 1 and 5', 400)
        except (ValueError, TypeError):
            return error_response(400, 'Rating must be a valid integer', 400)

        # Check if car exists
        try:
            car = CarListing.objects.get(id=car_id)
        except CarListing.DoesNotExist:
            return error_response(404, 'Car listing not found', 404)

        # Create the review
        review = CarReview.objects.create(
            car=car,
            rating=rating,
            comment=comment,
            user_email=user_email,
            user_name=user_name
        )

        # Calculate updated stats
        reviews = car.reviews.all()
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        total_reviews = reviews.count()

        return success_response({
            'review_id': review.id,
            'average_rating': round(average_rating, 1),
            'total_reviews': total_reviews,
            'message': 'Review submitted successfully'
        })

    except Exception as e:
        return error_response(500, f'Error submitting review: {str(e)}', 500)


@api_view(['GET'])
def get_car_reviews(request, car_id):
    """
    Get all reviews for a specific car listing.
    Returns reviews with pagination if needed.
    """
    try:
        car = CarListing.objects.get(id=car_id)
    except CarListing.DoesNotExist:
        return error_response(404, 'Car listing not found', 404)

    reviews = car.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    total_reviews = reviews.count()

    serializer = CarReviewSerializer(reviews, many=True, context={'request': request})

    return success_response({
        'average_rating': round(average_rating, 1),
        'total_reviews': total_reviews,
        'reviews': serializer.data
    })