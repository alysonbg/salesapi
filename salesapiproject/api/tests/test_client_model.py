from salesapiproject.api.models import Client


def test_create_client(db):
    assert Client.objects.create(name='Jon Snow',
                                 cpf='12345678901',
                                 birth_date='1994-08-11')


def test_str(db):
    client = Client.objects.create(name='Jon Snow',
                                   cpf='12345678901',
                                   birth_date='1994-08-11')

    assert 'Jon Snow' == str(client)
