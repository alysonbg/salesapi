from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


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


class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey('Client', related_name='clients', on_delete=models.PROTECT)
    seller = models.ForeignKey(UserModel, related_name='sellers', on_delete=models.PROTECT)
    order_date = models.DateField(auto_now=True)

    @property
    def total(self):
        sum_ = 0
        lines = self.orderlines.all()
        for line in lines:
            sum_ += line.total
        return sum_


class OrderLine(models.Model):
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name='orderlines', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.price * self.quantity
