from django.contrib import admin

from salesapiproject.api.models import ProductLot, Product, Order, OrderLine, Client

admin.site.register(ProductLot)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Client)
