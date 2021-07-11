import pytest
from salesapiproject.api.serializers import ProductCreateSerializer


@pytest.fixture
def serializer(product_lot):
    data = dict(name='Iphone 12 mini',
                lot=product_lot.id,
                color='red',
                description='Iphone 12 mini',
                cost='800.00')
    return ProductCreateSerializer(data=data)


def test_serializer_data(db, serializer, product_lot):
    serializer.is_valid()
    assert serializer.data == {
        'name': 'Iphone 12 mini',
        'lot': product_lot.id,
        'color': 'red',
        'description': 'Iphone 12 mini',
        'cost': '800.00'
    }
