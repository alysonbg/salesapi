import pytest
from django.shortcuts import reverse as r


@pytest.fixture
def get_response(db, auth_client, new_client):
    return auth_client.get(r('client-list'))


def test_get_response_status_code(get_response):
    assert get_response.status_code == 200


def test_get_response_body(get_response):
    assert 1 == len(get_response.data)


def test_get_unauthorize(db, client):
    response = client.get(r('client-list'))
    assert 401 == response.status_code


@pytest.fixture
def post_response(db, auth_client):
    data = {
        'name': 'Rob Stark',
        'cpf': '12345678901',
        'birth_date': '1994-04-01'
    }
    return auth_client.post(r('client-list'), data=data)


def test_post_response_status_code(post_response):
    assert 201 == post_response.status_code


def test_post_response_body(post_response):
    data = {
        'name': 'Rob Stark',
        'cpf': '12345678901',
        'birth_date': '1994-04-01'
    }

    assert data == post_response.data


def test_post_response_unauthorized(db, client):
    data = {
        'name': 'Rob Stark',
        'cpf': '12345678901',
        'birth_date': '1994-04-01'
    }
    response = client.post(r('client-list'), data=data)
    assert 401 == response.status_code


@pytest.fixture
def delete_response(db, auth_client, new_client):
    return auth_client.delete(r('client-detail', kwargs={'pk': new_client.pk}))


def test_delete_response_status_code(delete_response):
    assert 204 == delete_response.status_code


def delete_unauthorized(db, client, new_client):
    response = client.delete(r('client-detail', kwargs={'pk': new_client.pk}))

    assert 401 == response.status_code


@pytest.fixture
def patch_response(db, auth_client, new_client):
    data = {'manufacturing_date': '2021-07-19'}
    return auth_client.patch(r('client-detail', kwargs={'pk': new_client.pk}), data=data)


def test_patch_response_status_code(patch_response):
    assert 200 == patch_response.status_code


def test_patch_unauthorized(db, client, product_lot):
    data = {'manufacturing_date': '2021-07-19'}
    response = client.patch(r('client-detail', kwargs={'pk': product_lot.pk}), data=data)

    assert 401 == response.status_code
