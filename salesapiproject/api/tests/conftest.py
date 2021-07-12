from decimal import Decimal

import pytest

from salesapiproject.api.models import ProductLot, Product, Client, Order, OrderLine

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

UserModel = get_user_model()


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
def new_client(db):
    return Client.objects.create(name='Ned Stark',
                                 cpf='12345678901',
                                 birth_date='1994-07-11')


@pytest.fixture
def new_user(db):
    return UserModel.objects.create_superuser('admin', 'admin@admin.com', 'admin123')


@pytest.fixture
def order(db, products_with_lot, new_user, new_client):
    return Order.objects.create(client=new_client,
                                seller=new_user,)


@pytest.fixture
def orderlines(db, order, products_with_lot):
    return [
        OrderLine.objects.create(product=products_with_lot[0],
                                 order=order,
                                 price=Decimal(1200),
                                 quantity=2),
        OrderLine.objects.create(product=products_with_lot[1],
                                 order=order,
                                 price=Decimal(300),
                                 quantity=2)
    ]


@pytest.fixture
def auth_client(db, new_user):
    token = Token.objects.create(user=new_user)
    user = UserModel.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    return client
