import pytest
from salesapiproject.api.serializers import ProductLotSerializer


@pytest.fixture
def serializer():
    data = dict(code='lot123',
                manufacturing_date='2021-07-10',)
    return ProductLotSerializer(data=data)


def test_serializer_data(db, serializer):
    serializer.is_valid()
    serializer.save()

    assert serializer.data == {
            'code': 'lot123',
            'manufacturing_date': '2021-07-10',
            'products_quantity': 0,
        }
