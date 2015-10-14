from django.db import models
from sales.models import Sale
from abstract_classes.models import ProductMixin


class Boat(ProductMixin, models.Model):

    AVAILABLE   = 'A'
    SOLD_OUT    = 'S'
    PRE_SALE    = 'P'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (SOLD_OUT, 'Sold Out'),
        (PRE_SALE, 'Pre Sale'),
    )

    FISHING = 'F'
    BOWRIDER = 'B'
    PONTOON = 'P'
    WATERSPORTS = 'W'
    YACHT = 'Y'

    TYPE_CHOICES = (
        (FISHING, 'Fishing'),
        (BOWRIDER, 'Bowrider'),
        (PONTOON, 'Pontoon'),
        (WATERSPORTS, 'Watersports'),
        (YACHT, 'Yacht'),
    )

    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=BOWRIDER)
    cover_image = models.ImageField(upload_to='uploaded_images/boat_images', null=True, blank=True)