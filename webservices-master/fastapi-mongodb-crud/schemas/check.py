from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from db.models import Check
from .link import Link


class CheckCreateReqBody(BaseModel):
    id: UUID
    name: str
    version: str
    description: str
    lang: str
    params: list[str] | None = None
    func_body: str

    class Config:
        schema_extra = {
            'example': {
                'id': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                'name': 'sum_is_zero',
                'version': '0.0.1',
                'description': 'Checks if the sum of the amounts is equal to zero.',
                'lang': 'python',
                'params': ['amount_1: int', 'amount_2: int', 'amount_3: int'],
                'func_body': 'return (amount_1 + amount_2 + amount_3) == 0'
            }
        }

class CheckUpdateReqBody(BaseModel):
    name: str | None = None
    version: str | None = None
    description: str | None = None
    lang: str | None = None
    params: list[str] | None = None
    func_body: str | None = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'sum_is_zero',
                'version': '0.1.2',
                'description': 'Checks if the sum of the amounts is equal to zero.',
                'lang': 'python',
                'params': ['amounts: list[int]'],
                'func_body': 'return sum(amounts) == 0'
            }
        }

class CheckResBody(BaseModel):
    id: UUID 
    name: str
    version: str
    released: datetime
    description: str
    lang: str
    params: list[str] | None = None
    func_body: str

    links: list[Link] = []

    class Config:
        schema_extra = {
            'example': {
                'id': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                'name': 'sum_is_zero',
                'version': '0.0.1',
                'released': '2022-08-25T19:50:12.352719',
                'description': 'Checks if the sum of the amounts is equal to zero.',
                'lang': 'python',
                'params': ['amount_1: int', 'amount_2: int', 'amount_3: int'],
                'func_body': 'return (amount_1 + amount_2 + amount_3) == 0',
                'links': [
                    {
                        'href': '/checks/dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                        'rel': 'self',
                        'method': 'GET'
                    },
                    {
                        'href': '/checks/dbf2a72a-15cf-4fc6-a7fd-879f75989a6c/procedures',
                        'rel': 'procedures',
                        'method': 'GET'
                    }
                ]
            }
        }

class CheckListResBody(BaseModel):
    checks: list[Check] = []
    links: list[Link] = []