import pytest
from django.shortcuts import reverse as r


@pytest.fixture
def get_response(db, auth_client, orderlines):
    return auth_client.get(r('orderline-list'))


def test_get_response_status_code(get_response):
    assert get_response.status_code == 200


def test_get_response_body(get_response):
    assert 2 == len(get_response.data)


def test_get_unauthorized(db, client, products_with_lot):
    response = client.get(r('orderline-list'))
    assert 401 == response.status_code


@pytest.fixture
def post_response(db, auth_client, products_with_lot, order):
    product = products_with_lot[0]
    data = {'product': product.pk,
            'order': order.id,
            'price': '1200.00',
            'quantity': 2,
            }
    return auth_client.post(r('orderline-list'), data=data)


def test_post_response_status_code(post_response):
    assert post_response.status_code == 201


def test_post_response_body(post_response, products_with_lot, order):
    product = products_with_lot[0]
    data = {'product': product.id,
            'order': order.id,
            'price': '1200.00',
            'quantity': 2,
            }

    assert data == post_response.data


def test_fail_post_response(db, auth_client, products_with_lot, order):
    product = products_with_lot[0]
    data = {'product': product.id,
            'order': order.id,
            'quantity': 2,
            }
    response = auth_client.post(r('orderline-list'), data=data)

    assert 400 == response.status_code


def test_post_unauthorized(db, client, product_lot):
    data = {'name': 'Mac mini',
            'lot': product_lot.id,
            'color': 'white',
            'description': 'A mac mini m1',
            'cost': '1200.00'}
    response = client.post(r('orderline-list'), data=data)
    assert 401 == response.status_code


@pytest.fixture
def delete_response(db, auth_client, orderlines):
    orderline = orderlines[0]
    return auth_client.delete(r('order-detail', kwargs={'pk': orderline.pk}))


def test_delete_response_status_code(delete_response):
    assert 204 == delete_response.status_code


def test_fail_to_delete_invalid_product(db, auth_client):
    response = auth_client.delete(r('order-detail', kwargs={'pk': 999}))
    assert 404 == response.status_code


def test_delete_unauthorized(db, client):
    response = client.delete(r('order-detail', kwargs={'pk': 999}))
    assert 401 == response.status_code


@pytest.fixture
def patch_response(db, auth_client, orderlines):
    orderline = orderlines[0]
    data = {'price': '100'}
    return auth_client.delete(r('order-detail', kwargs={'pk': orderline.id}), data)


def test_patch_response_status_code(patch_response):
    assert 204 == patch_response.status_code


def test_patch_unauthorized(db, client, products_with_lot):
    order = products_with_lot[0]
    data = {'price': '100'}
    response = client.delete(r('order-detail', kwargs={'pk': order.id}), data)
    assert 401 == response.status_code


def test_put_not_allowed(db, auth_client, products_with_lot, product_lot):
    order = products_with_lot[0]
    data = {'name': 'Mac pro',
            'lot': product_lot.id,
            'description': 'A mac pro',
            'cost': '2500.00'}
    response = auth_client.put(r('order-detail', kwargs={'pk': order.id}), data)
    assert 405 == response.status_code
