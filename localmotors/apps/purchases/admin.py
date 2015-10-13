from django.contrib import admin

from purchases.models import Purchase, PurchaseItem

admin.site.register(Purchase)
admin.site.register(PurchaseItem)
