from django.db import models


class HeroBanner(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    hero_image = models.ImageField(
        upload_to='page_content/hero_banners/',
        help_text='Recommended size: 1700x900px'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ScrollBar(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class AboutContent(models.Model):
    title = models.CharField(
        max_length=255,
        default="Why Choose Isam Auto"
    )
    description = models.TextField(
        default=(
            "Over the Years, we have done a great amount of research on the market to determine our customers’ needs. "
            "Based on the report, we have been buying varieties of vehicles with different price ranges to accommodate those needs. "
            "We keep offering our vehicles at less than the market, because we believe in building long-term relationships "
            "with our customers through our value based repair services."
        )
    )

    feature_1_title = models.CharField(max_length=255, default="Free Buyer’s Inspection")
    feature_2_title = models.CharField(max_length=255, default="Interest Free Payment Flexibility")
    feature_3_title = models.CharField(max_length=255, default="59 Seconds of Paperwork")

    content_title_1 = models.CharField(max_length=255, default="Free Buyer’s Inspection")
    content_description_1 = models.TextField(default="Know exactly what you are buying")
    content_icon_1 = models.ImageField(upload_to='about/icons/', blank=True, null=True)

    content_title_2 = models.CharField(max_length=255, default="Payment Flexibility")
    content_description_2 = models.TextField(default="Not enough budget? Buy & Pay Later without Paying any Interest")
    content_icon_2 = models.ImageField(upload_to='about/icons/', blank=True, null=True)

    content_title_3 = models.CharField(max_length=255, default="Trade on Spot")
    content_description_3 = models.TextField(default="Wanna Get Rid of your Humpty Dumpty? Try Us!")
    content_icon_3 = models.ImageField(upload_to='about/icons/', blank=True, null=True)

    content_image1 = models.ImageField(upload_to='about/images/', blank=True, null=True)
    content_image2 = models.ImageField(upload_to='about/images/', blank=True, null=True)

    def __str__(self):
        return self.title
