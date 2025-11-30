from django.urls import path
from .views import (
    get_car_listings, get_car_types, get_car_brands, get_car_body_types,
    get_fuel_types, get_drive_types, get_gear_types, get_owner_types,
    get_features, get_car_models, get_model_years, get_car_dealers,
    get_car_images, get_car_detail
)

urlpatterns = [
    path('car-listings/',      get_car_listings,   name='get_car_listings'),
    path('car-listings/<slug:slug>/',      get_car_detail,   name='get_car_detail'),
    path('car-types/',         get_car_types,      name='get_car_types'),
    path('car-brands/',        get_car_brands,     name='get_car_brands'),
    path('body-types/',        get_car_body_types, name='get_car_body_types'),
    path('fuel-types/',        get_fuel_types,     name='get_fuel_types'),
    path('drive-types/',       get_drive_types,    name='get_drive_types'),
    path('gear-types/',        get_gear_types,     name='get_gear_types'),
    path('owner-types/',       get_owner_types,    name='get_owner_types'),
    path('features/',          get_features,       name='get_features'),
    path('car-models/',        get_car_models,     name='get_car_models'),
    path('model-years/',       get_model_years,    name='get_model_years'),
    path('car-dealers/',       get_car_dealers,    name='get_car_dealers'),
    # path('car-images/',        get_car_images,     name='get_car_images'),
]
