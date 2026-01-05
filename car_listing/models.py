from django.db import models
from django.utils.text import slugify


class CarType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    title = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='car_brands/logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CarBodyType(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='car_body/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FuelType(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DriveType(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class GearType(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OwnerType(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CarModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ModelYear(models.Model):
    year = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.year)


class CarDealer(models.Model):
    name = models.CharField(max_length=191, unique=True)
    image = models.ImageField(upload_to='car_dealers/images/', blank=True, null=True)
    location_name = models.CharField(max_length=191, null=True, blank=True)
    location = models.TextField(help_text="Google Maps embed code")
    contact_number = models.CharField(max_length=20, unique=True)
    whatsapp_link = models.URLField(unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CarListing(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('On Sale', 'On Sale'),
        ('Featured', 'Featured'),
        ('Sold Car', 'Sold Car'),
    ]
    
    title = models.CharField(max_length=191, unique=True)
    slug = models.SlugField(max_length=191, unique=True, blank=True)
    video_url = models.URLField(max_length=191, null=True, blank=True)
    carfax = models.FileField(upload_to='car_listings/carfax/', null=True, blank=True)

    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    body_type = models.ForeignKey(CarBodyType, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE)
    gear_type = models.ForeignKey(GearType, on_delete=models.CASCADE)
    owner_type = models.ForeignKey(OwnerType, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    model_year = models.ForeignKey(ModelYear, on_delete=models.CASCADE)
    dealer = models.ForeignKey(CarDealer, on_delete=models.CASCADE)

    features = models.ManyToManyField(Feature, blank=True)
    mileage = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_installment_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    installment_month = models.PositiveIntegerField(null=True, blank=True)
    # original_price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField()
    cylinders = models.PositiveIntegerField()
    stock_number = models.CharField(max_length=100, unique=True)
    vin_number = models.CharField(max_length=100, unique=True)
    engine_size = models.CharField(max_length=50)
    doors = models.PositiveIntegerField()
    interior_colors = models.CharField(max_length=100)
    exterior_colors = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    comfort_convenience = models.TextField(null=True, blank=True)
    interior_description = models.TextField(null=True, blank=True)
    exterior_description = models.TextField(null=True, blank=True)
    safety = models.TextField(null=True, blank=True)
    entertainment_communication = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class CarImage(models.Model):
    car = models.ForeignKey(CarListing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_listings/images/')
    alt_text = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False, help_text="Tick to make this the listing's featured image")

    def __str__(self):
        return f"Image for {self.car.title}"


class CarReview(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    car = models.ForeignKey(CarListing, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Car Review'
        verbose_name_plural = 'Car Reviews'

    def __str__(self):
        return f"Review by {self.user_name} for {self.car.title} ({self.rating}/5)"
