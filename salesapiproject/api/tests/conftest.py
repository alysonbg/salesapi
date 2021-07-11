import pytest

from salesapiproject.api.models import ProductLot, Product


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
