import pytest
from django.shortcuts import reverse as r


@pytest.fixture
def get_response(db, auth_client, product_lot):
    return auth_client.get(r('productlot-list'))


def test_get_response_status_code(get_response):
    assert get_response.status_code == 200


def test_get_response_body(get_response):
    assert 1 == len(get_response.data)


def test_get_unauthorize(db, client):
    response = client.get(r('productlot-list'))
    assert 401 == response.status_code


@pytest.fixture
def post_response(db, auth_client):
    data = {
        'code': 'testeproductlot123',
        'manufacturing_date': '2021-07-11'
    }
    return auth_client.post(r('productlot-list'), data=data)


def test_post_response_status_code(post_response):
    assert 201 == post_response.status_code


def test_post_response_body(post_response):
    data = {
        'code': 'testeproductlot123',
        'manufacturing_date': '2021-07-11',
        'products_quantity': 0
    }

    assert data == post_response.data


def test_post_response_unauthorized(db, client):
    data = {
        'code': 'testeproductlot123',
        'manufacturing_date': '2021-07-11'
    }
    response = client.post(r('productlot-list'), data=data)
    assert 401 == response.status_code


@pytest.fixture
def delete_response(db, auth_client, product_lot):
    return auth_client.delete(r('productlot-detail', kwargs={'pk': product_lot.pk}))


def test_delete_response_status_code(delete_response):
    assert 204 == delete_response.status_code


def delete_unauthorized(db, client, product_lot):
    response = client.delete(r('productlot-detail', kwargs={'pk': product_lot.pk}))

    assert 401 == response.status_code


@pytest.fixture
def patch_response(db, auth_client, product_lot):
    data = {'manufacturing_date': '2021-07-19'}
    return auth_client.patch(r('productlot-detail', kwargs={'pk': product_lot.pk}), data=data)


def test_patch_response_status_code(patch_response):
    assert 200 == patch_response.status_code


def test_patch_unauthorized(db, client, product_lot):
    data = {'manufacturing_date': '2021-07-19'}
    response = client.patch(r('productlot-detail', kwargs={'pk': product_lot.pk}), data=data)

    assert 401 == response.status_code


def test_put_not_allowed(db, auth_client, product_lot):
    data = {'code': 'New code',
            'manufacturing_date': '2021-07-19',
            }
    response = auth_client.put(r('product-detail', kwargs={'pk': product_lot.id}), data)
    assert 405 == response.status_code
