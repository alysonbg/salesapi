from salesapiproject.api.serializers import ProductLotSerializer


def test_serializer_data(db, product_lot):
    serializer = ProductLotSerializer(product_lot)

    assert serializer.data == {
            'code': 'lot123',
            'manufacturing_date': '2021-07-10',
            'products_quantity': 0,
        }
