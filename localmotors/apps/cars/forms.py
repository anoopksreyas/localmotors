from django import forms
from cars.models import *

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'color', 'description', 'miles', 'msrp',
                  'retail_price', 'inventory_count', 'transmission', 'status', 'drive_train',
                  'sku', 'trim', 'engine_type', 'active')
    

