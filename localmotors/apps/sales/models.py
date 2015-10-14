from django.db import models


class Sale(models.Model):

    PERCENT = 'P'
    DOLLAR = 'D'

    DISCOUNT_TYPE_CHOICES = (
        (PERCENT, 'Percent'),
        (DOLLAR, 'Dollar'),
    )

    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    discount_type = models.CharField(max_length=1, choices=DISCOUNT_TYPE_CHOICES, default=PERCENT)
    discount_amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
