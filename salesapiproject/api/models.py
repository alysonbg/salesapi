from django.db import models


class ProductLot(models.Model):
    code = models.CharField(max_length=100, unique=True)
    manufacturing_date = models.DateField()

    @property
    def products_quantity(self):
        return self.products.count()

    def __str__(self):
        return self.code


class Product(models.Model):
    name = models.CharField(max_length=255)
    lot = models.ForeignKey('ProductLot', on_delete=models.CASCADE, related_name='products')
    color = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
