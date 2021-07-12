from salesapiproject.api.models import Product, ProductLot, Client, Order, OrderLine
from salesapiproject.api.serializers import ProductSerializer, ProductCreateSerializer, ProductLotSerializer, \
    ClientSerializer, OrderSerializer, OrderCreateSerializer, OrderLineSerializer, OrderLineCreateSerializer

from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update',
            'delete'
        ]
        if self.action in actions:
            return ProductCreateSerializer
        return self.serializer_class


class ProductLotViewSet(viewsets.ModelViewSet):
    queryset = ProductLot.objects.all()
    serializer_class = ProductLotSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update',
            'delete'
        ]
        if self.action in actions:
            return OrderCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class OrderLineViewSet(viewsets.ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update',
            'delete'
        ]
        if self.action in actions:
            return OrderLineCreateSerializer
        return self.serializer_class
