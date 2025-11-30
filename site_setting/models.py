from django.db import models

class Settings(models.Model):
    site_title = models.CharField(
        max_length=255,
        default="ISAM'S AUTO SALES & REPAIRS"
    )
    moto = models.CharField(
        max_length=255,
        blank=True,
        default="What Drives You"
    )
    description1 = models.TextField(
        blank=True,
        default=(
            "Over the years, we have done extensive research on the market to "
            "determine our customers’ needs. Based on that, we’ve sourced a wide "
            "variety of pre-owned vehicles at competitive prices—because we believe "
            "in building long-term relationships through value-based service."
        )
    )
    description2 = models.TextField(
        blank=True,
        default=(
            "• Free Buyer’s Inspection\n"
            "• Interest-Free Payment Flexibility\n"
            "• 59 Seconds of Paperwork"
        )
    )
    keywords = models.TextField(
        blank=True,
        default="pre-owned cars, auto sales, car repair, Saskatoon"
    )

    contact_email = models.EmailField(default="info@isamauto.ca")
    site_reciviable_email = models.EmailField(default="info@isamauto.ca")
    support_email = models.EmailField(default="info@isamauto.ca")
    contact_number = models.CharField(
        max_length=20,
        blank=True,
        default="+1 306 974 4820"
    )
    address = models.TextField(
        blank=True,
        default="1009 20th St. W, Saskatoon, SK S7M 0Y6, Canada"
    )
    address_embaded_code = models.TextField(
        blank=True,
        default=(
            '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2449.462765143648!2d-106.6853355!3d52.12590309999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5304f7341a317c93%3A0x8fa3456f6eeb1ead!2sIsam&#39;s%20auto%20repair!5e0!3m2!1sen!2sbd!4v1746353887595!5m2!1sen!2sbd" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
        )
    )

    facebook  = models.URLField(blank=True, default="https://www.facebook.com/isamauto")
    x         = models.URLField(blank=True, default="https://twitter.com/isamauto")
    instagram = models.URLField(blank=True, default="https://www.instagram.com/isamauto")
    linkedin  = models.URLField(blank=True, default="https://www.linkedin.com/company/isamauto")
    youtube   = models.URLField(blank=True, default="https://www.youtube.com/channel/UC_ISAM_AUTO")
    whatsapp  = models.CharField(max_length=20, blank=True, default="+1 306 974 4820")

    logo            = models.ImageField(upload_to='settings/', blank=True, null=True)
    favicon         = models.ImageField(upload_to='settings/', blank=True, null=True)
    secondary_logo  = models.ImageField(upload_to='settings/', blank=True, null=True)

    def __str__(self):
        return self.site_title
