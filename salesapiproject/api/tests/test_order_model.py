from decimal import Decimal

import pytest
from salesapiproject.api.models import Order, OrderLine


def test_order_create(new_client, new_user):
    assert Order.objects.create(client=new_client,
                                seller=new_user,)


@pytest.fixture
def order(db, new_client, new_user):
    return Order.objects.create(client=new_client,
                                seller=new_user)


def test_order_total(db, order, products_with_lot):
    OrderLine.objects.create(product=products_with_lot[0],
                             order=order,
                             price=1200.00,
                             quantity=2)
    OrderLine.objects.create(product=products_with_lot[1],
                             order=order,
                             price=600.00,
                             quantity=1)

    assert order.total == Decimal(3000)
