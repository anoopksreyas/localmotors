from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from purchases.models import Purchase, PurchaseItem, PurchaseMixin
from django.contrib.contenttypes.models import ContentType


class PurchaseTestCase(TestCase):

    def setUp(self):
        self.content_type = ContentType.objects.get(app_label='auth', model='permission')
        
        self.user = User.objects.create_user(
            'local_motors',
            'local_m@gmail.com',
            'test123'
            )
        
        self.content_type = ContentType.objects.get(app_label='auth', model='permission')
        
        self.purchase_item = PurchaseItem.objects.create(quantity = 20,
                                                         content_type = self.content_type,
                                                         object_id = 123)
        
        self.purchase = Purchase.objects.create(user = self.user,
                                                invoice_number = 12345,
                                                status = 'R',
                                                total = 40
                                                )
        
    def test_get_total_invoice_item(self):
        self.client.login(username='local_motors', password='test123')
        self.assertEqual(self.purchase.total, 40)