from rest_framework import serializers

from salesapiproject.api.models import Product, ProductLot, Client, Order, OrderLine


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


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['name', 'cpf', 'birth_date']


class OrderLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderLine
        fields = ['product', 'price', 'quantity']


class OrderCreateSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['client', 'seller', 'total']
        read_only_fields = ('seller',)


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    # orderlines = OrderLineSerializer(source='orderlines')

    class Meta:
        model = Order
        fields = ['client', 'seller', 'total']
