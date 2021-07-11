from salesapiproject.api.models import ProductLot


def test_create_lot(db):
    assert ProductLot.objects.create(
        code='product123',
        manufacturing_date='2021-07-10',
    )


def test_amount_products_using_a_lot(db, product_lot, products_with_lot):
    assert product_lot.products_quantity == 2


def test_str(product_lot):
    assert 'lot123' == str(product_lot)
