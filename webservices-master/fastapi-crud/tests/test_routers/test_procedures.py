from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from server.routers import procedures
# To be able to import like this create setup.py then pip install -e .

from datetime import datetime


def start_application():
    test_app = FastAPI()
    test_app.include_router(
        procedures.router,
        prefix='/procedures'
        )
    
    return test_app

client = TestClient(start_application())


def test_read_procedures():
    response = client.get('/procedures/')
    
    assert response.status_code == status.HTTP_200_OK

def test_create_procedure():
    body = {
        'uuid': '46f7efa5-ed1b-464f-bac0-8de880a390fd',
        'name': 'some_fancy_name',
        'version': '0.0.1',
        'description': 'The scope of this procedure is defined by some theory about how to validate related data.',
        'checks': [
            'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
            '87bf38ab-d853-470b-b6a0-129867378a05',
            '9c356f92-7b37-4ed5-bf88-3806cb4f5ad1',
            '00d31962-d426-4bde-86bd-1682b2a3d582'
            ]
    }

    response = client.post('/procedures/', json=body)

    assert response.status_code == status.HTTP_201_CREATED

def test_create_procedure_already_exists():
    body = {
        'uuid': '46f7efa5-ed1b-464f-bac0-8de880a390fd',
        'name': 'some_fancy_name',
        'version': '0.0.1',
        'description': 'The scope of this procedure is defined by some theory about how to validate related data.',
        'checks': [
            'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
            '87bf38ab-d853-470b-b6a0-129867378a05',
            '9c356f92-7b37-4ed5-bf88-3806cb4f5ad1',
            '00d31962-d426-4bde-86bd-1682b2a3d582'
            ]
    }

    response = client.post('/procedures/', json=body)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_read_procedure_not_existing_uuid():
    id = '00d31962-d426-4bde-86bd-1682b2a3d582'
    response = client.get(f'/procedures/{id}')

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_procedure():
    id = '46f7efa5-ed1b-464f-bac0-8de880a390fd'
    body = {
        'uuid': '46f7efa5-ed1b-464f-bac0-8de880a390fd',
        'checks': [
            'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
            '00d31962-d426-4bde-86bd-1682b2a3d582'
            ]
    }
    
    response = client.put(f'/procedures/{id}', json=body)

    assert response.status_code == status.HTTP_200_OK

def test_update_procedure_not_existing_uuid():
    id = '46f7efa5-ed1b-464f-bac0-8de880a390fa'
    body = {
        'uuid': '46f7efa5-ed1b-464f-bac0-8de880a390fd',
        'checks': [
            'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
            '00d31962-d426-4bde-86bd-1682b2a3d582'
            ]
    }
    
    response = client.put(f'/procedures/{id}', json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_procedure():
    id = '46f7efa5-ed1b-464f-bac0-8de880a390fd'
    response = client.delete(f'/procedures/{id}')

    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_delete_procedure_not_existing_uuid():
    id = '46f7efa5-ed1b-464f-bac0-8de880a390fd'
    response = client.delete(f'/procedures/{id}')

    assert response.status_code == status.HTTP_404_NOT_FOUND