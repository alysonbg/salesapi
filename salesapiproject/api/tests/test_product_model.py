from salesapiproject.api.models import Product


def test_create_product(product_lot):
    assert Product.objects.create(
        name='Macbook air',
        lot=product_lot,
        color='gray',
        description='Latest Macbook air',
        cost='1000'
    )
