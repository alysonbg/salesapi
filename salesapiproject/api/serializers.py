from rest_framework import serializers

from salesapiproject.api.models import Product, ProductLot


class ProductLotSerializer(serializers.ModelSerializer):
    products_quantity = serializers.ReadOnlyField()

    class Meta:
        model = ProductLot
        fields = ['code', 'manufacturing_date', 'products_quantity']


class ProductSerializer(serializers.ModelSerializer):
    lot = ProductLotSerializer()

    class Meta:
        model = Product
        fields = ['name', 'lot', 'color', 'description', 'cost']


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'lot', 'color', 'description', 'cost']
