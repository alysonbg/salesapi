from salesapiproject.api.models import Product
from salesapiproject.api.serializers import ProductSerializer, ProductCreateSerializer
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
