from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User
from cars.models import Car
from sales.models import Sale
from django.contrib.contenttypes.models import ContentType

class CarsTestCase(TestCase):
    
    def setUp(self):
        self.content_type = ContentType.objects.get(app_label='auth', model='permission')
        
        self.user = User.objects.create_user(
            'local_motors',
            'local_m@gmail.com',
            'test123'
            )
        
        self.content_type = ContentType.objects.get(app_label='auth', model='permission')
        
        self.sale = Sale.objects.create(title = 'Sales',
                                        description = 'test desc',
                                        discount_type = 'P',
                                        discount_amount = 25000,
                                        )
        
        self.car = Car.objects.create(make = 'Maruti',
                                      model = 'Swift',
                                      year = '2015',
                                      color = 'Blue',
                                      description = 'Maruti Swift',
                                      inventory_count = 20,
                                      transmission = 'A',
                                      active = 1
                                      )
        
    def test_get_discounted_price(self):
        self.client.login(username='local_motors', password='test123')
        self.assertEqual(self.sale.discount_amount, 25000)
