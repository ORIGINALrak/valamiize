from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from server.routers import checks
# To be able to import like this create setup.py then pip install -e .

from datetime import datetime


def start_application():
    test_app = FastAPI()
    test_app.include_router(
        checks.router,
        prefix='/checks'
        )
    
    return test_app

client = TestClient(start_application())


def test_read_checks():
    response = client.get('/checks/')
    
    assert response.status_code == status.HTTP_200_OK

def test_create_check():
    body = {
        'uuid': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
        'name': 'sum_is_zero',
        'version': '0.0.1',
        'description': 'Checks if the sum of the amounts is equal to zero.',
        'lang': 'python',
        'params': ['amount_1: int', 'amount_2: int', 'amount_3: int'],
        'func_body': 'return (amount_1 + amount_2 + amount_3) == 0'
    }

    response = client.post('/checks/', json=body)

    assert response.status_code == status.HTTP_201_CREATED

def test_create_check_already_exists():
    body = {
        'uuid': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
        'name': 'sum_is_zero',
        'version': '0.0.1',
        'description': 'Checks if the sum of the amounts is equal to zero.',
        'lang': 'python',
        'params': ['amount_1: int', 'amount_2: int', 'amount_3: int'],
        'func_body': 'return (amount_1 + amount_2 + amount_3) == 0'
    }

    response = client.post('/checks/', json=body)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_read_check_not_existing_uuid():
    id = 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6d'
    response = client.get(f'/checks/{id}')

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_check():
    id = 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c'
    body = {
        'uuid': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
        'version': '1.0.0'
    }
    
    response = client.put(f'/checks/{id}', json=body)

    assert response.status_code == status.HTTP_200_OK

def test_update_check_not_existing_uuid():
    id = 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6d'
    body = {
        'uuid': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6d',
        'version': '1.0.0'
    }
    
    response = client.put(f'/checks/{id}', json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_check():
    id = 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c'
    response = client.delete(f'/checks/{id}')

    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_delete_check_not_existing_uuid():
    id = 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c'
    response = client.delete(f'/checks/{id}')

    assert response.status_code == status.HTTP_404_NOT_FOUND