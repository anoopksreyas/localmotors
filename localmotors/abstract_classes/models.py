from django.db import models
from sales.models import Sale

class ProductMixin(models.Model):
    make = models.CharField(max_length=55, null=True, blank=True)
    model = models.CharField(max_length=55, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    msrp = models.DecimalField(blank=True, null=True, default=0.00, decimal_places=2, max_digits=10)
    retail_price = models.DecimalField(blank=True, null=True, default=0.00, decimal_places=2, max_digits=10)
    inventory_count = models.IntegerField(default=0)
    length = models.CharField(max_length=30, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    hull_material = models.CharField(max_length=50, null=True, blank=True)
    sku = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    sales = models.ManyToManyField(Sale, null=True, blank=True)
    
    class Meta:
        abstract = True
    
    
