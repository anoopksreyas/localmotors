from django.db import models
from sales.models import Sale
from abstract_classes.models import ProductMixin

class Car(ProductMixin, models.Model):

    AVAILABLE   = 'A'
    SOLD_OUT    = 'S'
    PRE_SALE    = 'P'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (SOLD_OUT, 'Sold Out'),
        (PRE_SALE, 'Pre Sale'),
    )

    MANUAL = 'M'
    AUTOMATIC = 'A'

    TRANSMISSION_CHOICES = (
        (MANUAL, 'Manual'),
        (AUTOMATIC, 'Automatic'),
    )

    FRONT_WHEEL = 'FWD'
    REAR_WHEEL = 'RWD'
    ALL_WHEEL = 'AWD'
    FOUR_WHEEL = '4WD'

    DRIVE_TRAIN_CHOICES = (
        (FRONT_WHEEL, 'Front-wheel drive'),
        (REAR_WHEEL, 'Rear-wheel drive'),
        (ALL_WHEEL, 'All-wheel drive'),
        (FOUR_WHEEL, 'Four-wheel drive'),
    )

    color = models.CharField(max_length=25, null=True, blank=True)
    miles = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES, default=AUTOMATIC)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)
    drive_train = models.CharField(max_length=3, choices=DRIVE_TRAIN_CHOICES, default=FRONT_WHEEL)
    trim = models.CharField(max_length=15, null=True, blank=True)
    engine_type = models.CharField(max_length=35, null=True, blank=True)
    cover_image = models.ImageField(upload_to='uploaded_images/car_images', null=True, blank=True)

    def is_available(self):
        return self.status == self.AVAILABLE

    def is_sold_out(self):
        return self.status == self.SOLD_OUT

    def is_automatic(self):
        return self.transmission == self.AUTOMATIC
    
    ########## Method to return discounted price if it on Sales ########
    def get_discounted_price(self):
        if self.sales:
            return self.sales__discount_amount
    
