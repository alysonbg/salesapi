import pytest

from salesapiproject.api.serializers import ClientSerializer


@pytest.fixture
def serializer():
    data = dict(name='Jon Snow',
                cpf='12345678901',
                birth_date='1993-07-01')

    return ClientSerializer(data=data)


def test_serializer_data(serializer):
    serializer.is_valid()
    data = {
        'name': 'Jon Snow',
        'cpf': '12345678901',
        'birth_date': '1993-07-01'}
    assert data == serializer.data
