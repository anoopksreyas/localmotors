from rest_framework import serializers
from cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description', 'retail_price', 'inventory_count')