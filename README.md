# salesapi
[![Python application](https://github.com/alysonbg/salesapi/actions/workflows/django_project.yml/badge.svg)](https://github.com/alysonbg/salesapi/actions/workflows/django_project.yml)

## Como acessar os endpoints:
1. Crie um usuário novo.
2. Executar a aplicação   
3. Faça uma requisição para conseguir um novo token
4. Salve o token.

```console
pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver
curl -d 'username=usuario&password=senha' http://127.0.0.1:8000/api-token-auth/
```

## Endpoints:
/api-token-auth/
```console
curl -d 'username=usuario&password=senha' http://127.0.0.1:8000/api-token-auth/
```

Endpoint para criar ou retornar um token.

## Products
GET /api/products/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/products/
```

POST /api/products/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/products/
```

DELETE /api/products/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/products/
```

PATCH /api/products/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/products/
```

## Orders
GET /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orders/
```

POST /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orders/
```

DELETE /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orders/
```

PATCH /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orders/
```

## OrderLines
GET /api/orderslines/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orderslines/
```

POST /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orderslines/
```

DELETE /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orderslines/
```

PATCH /api/orders/
```console
curl -H "Authorization: Token seu token" http://127.0.0.1:8000/api/orderslines/
```


