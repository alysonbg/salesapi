import pytest
from salesapiproject.api.models import Order, OrderLine


@pytest.fixture
def order(db, new_client, new_user):
    return Order.objects.create(client=new_client,
                                seller=new_user,
                                )


def test_create(products_with_lot, order):
    product = products_with_lot[0]
    assert OrderLine.objects.create(product=product,
                                    order=order,
                                    price='1200.00',
                                    quantity=2)


def test_total(products_with_lot, order):
    product = products_with_lot[0]
    order_line = OrderLine.objects.create(product=product,
                                          order=order,
                                          price=1200.00,
                                          quantity=2)
    assert 2400.00 == order_line.total

