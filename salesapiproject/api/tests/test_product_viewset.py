import pytest
from django.shortcuts import reverse as r


@pytest.fixture
def get_response(db, auth_client, products_with_lot):
    return auth_client.get(r('product-list'))


def test_get_response_status_code(get_response):
    assert get_response.status_code == 200


def test_get_response_body(get_response):
    assert 2 == len(get_response.data)


def test_get_unauthorized(db, client, products_with_lot):
    response = client.get(r('product-list'))
    assert 401 == response.status_code


@pytest.fixture
def post_response(db, auth_client, product_lot):
    data = {'name': 'Mac mini',
            'lot': product_lot.id,
            'color': 'white',
            'description': 'A mac mini m1',
            'cost': '1200.00'}
    return auth_client.post(r('product-list'), data=data)


def test_post_response_status_code(post_response):
    assert post_response.status_code == 201


def test_post_response_body(post_response, product_lot):
    data = {'name': 'Mac mini',
            'lot': product_lot.id,
            'color': 'white',
            'description': 'A mac mini m1',
            'cost': '1200.00'}

    assert data == post_response.data


def test_fail_post_response(db, auth_client, product_lot):
    data = {'name': 'Mac mini',
            'lot': product_lot.id,
            'description': 'A mac mini m1',
            'cost': '1200.00'}
    response = auth_client.post(r('product-list'), data=data)

    assert 400 == response.status_code


def test_post_unauthorized(db, client, product_lot):
    data = {'name': 'Mac mini',
            'lot': product_lot.id,
            'color': 'white',
            'description': 'A mac mini m1',
            'cost': '1200.00'}
    response = client.post(r('product-list'), data=data)
    assert 401 == response.status_code


@pytest.fixture
def delete_response(db, auth_client, products_with_lot):
    product = products_with_lot[0]
    return auth_client.delete(r('product-detail', kwargs={'pk': product.id}))


def test_delete_response_status_code(delete_response):
    assert 204 == delete_response.status_code


def test_fail_to_delete_invalid_product(db, auth_client):
    response = auth_client.delete(r('product-detail', kwargs={'pk': 999}))
    assert 404 == response.status_code


def test_delete_unauthorized(db, client):
    response = client.delete(r('product-detail', kwargs={'pk': 999}))
    assert 401 == response.status_code


@pytest.fixture
def patch_response(db, auth_client, products_with_lot):
    product = products_with_lot[0]
    data = {'name': 'Macbook pro'}
    return auth_client.delete(r('product-detail', kwargs={'pk': product.id}), data)


def test_patch_response_status_code(patch_response):
    assert 204 == patch_response.status_code


def test_patch_unauthorized(db, client, products_with_lot):
    product = products_with_lot[0]
    data = {'name': 'Macbook pro'}
    response = client.delete(r('product-detail', kwargs={'pk': product.id}), data)
    assert 401 == response.status_code


def test_put_not_allowed(db, auth_client, products_with_lot, product_lot):
    product = products_with_lot[0]
    data = {'name': 'Mac pro',
            'lot': product_lot.id,
            'description': 'A mac pro',
            'cost': '2500.00'}
    response = auth_client.put(r('product-detail', kwargs={'pk': product.id}), data)
    assert 405 == response.status_code
