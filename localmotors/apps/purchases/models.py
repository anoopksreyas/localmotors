from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class PurchaseItem(models.Model):

    quantity = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Purchase(models.Model):

    SHIPPED = 'S'
    RECEIVED = 'R'
    PROCESSING = 'P'
    DELAYED = 'D'
    CANCELLED = 'C'
    FULFILLED = 'F'

    STATUS_CHOICES = (
        (RECEIVED, 'Received'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELAYED, 'Delayed'),
        (CANCELLED, 'Cancelled'),
        (FULFILLED, 'Fullfilled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    invoice_number = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=RECEIVED)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(PurchaseItem)
    total = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    
####################### Model mixin to calculate total items for an invoice ############

class PurchaseMixin(Purchase):
    
    def get_total_invoice_item(self):
        return self.total




