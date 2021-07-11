import pytest

from salesapiproject.api.models import ProductLot, Product
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


@pytest.fixture
def product_lot(db):
    return ProductLot.objects.create(
        code='lot123',
        manufacturing_date='2021-07-10'
    )


@pytest.fixture
def products_with_lot(db, product_lot):
    return [
        Product.objects.create(
            name='Iphone 12 mini',
            lot=product_lot,
            color='red',
            description='Iphone 12 mini',
            cost='800'
        ),
        Product.objects.create(
            name='Airpods',
            lot=product_lot,
            color='gray',
            description='Airpods',
            cost='200'
        ),
    ]


@pytest.fixture
def auth_client(db):
    UserModel = get_user_model()
    user = UserModel.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    return client
