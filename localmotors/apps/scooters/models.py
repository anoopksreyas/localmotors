from django.db import models
from sales.models import Sale
from abstract_classes.models import ProductMixin


class Scooter(ProductMixin, models.Model):

    AVAILABLE   = 'A'
    SOLD_OUT    = 'S'
    PRE_SALE    = 'P'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (SOLD_OUT, 'Sold Out'),
        (PRE_SALE, 'Pre Sale'),
    )

    color = models.CharField(max_length=25, null=True, blank=True)
    miles = models.IntegerField(blank=True, null=True)
    engine_size = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)
    engine_type = models.CharField(max_length=200, null=True, blank=True)
    cover_image = models.ImageField(upload_to='uploaded_images/scooter_images', null=True, blank=True)
