from beanie import Document
from datetime import datetime
from uuid import UUID


class Check(Document):
    id: UUID 
    name: str
    version: str
    released: datetime
    description: str
    lang: str
    params: list[str] | None = None
    func_body: str

    class Settings:
        name = 'checks'

    class Config:
        schema_extra = {
            "example": {
                'id': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                'name': 'sum_is_zero',
                'version': '0.0.1',
                'released': datetime.now(),
                'description': 'Checks if the sum of the amounts is equal to zero.',
                'lang': 'python',
                'params': ['amount_1: int', 'amount_2: int', 'amount_3: int'],
                'func_body': 'return (amount_1 + amount_2 + amount_3) == 0'
            }
        }


class Procedure(Document):
    id: UUID
    name: str
    version: str
    released: datetime
    description: str
    checks: list[UUID] | None = None

    class Settings:
        name = 'procedures'

    class Config:
        schema_extra = {
            'example': {
                'id': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                'name': 'sum_is_zero',
                'version': '0.0.1',
                'released': datetime.now(),
                'description': 'The scope of this procedure is defined by some theory about how to validate related data.',
                'checks': [
                    'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                    '87bf38ab-d853-470b-b6a0-129867378a05',
                    '9c356f92-7b37-4ed5-bf88-3806cb4f5ad1',
                    '00d31962-d426-4bde-86bd-1682b2a3d582'
                ]
            }
        }