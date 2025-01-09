from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from db.models import Procedure
from .link import Link


class ProcedureCreateReqBody(BaseModel):
    id: UUID
    name: str
    version: str
    description: str
    checks: list[UUID]

    class Config:
        schema_extra = {
            'example': {
                'id': '46f7efa5-ed1b-464f-bac0-8de880a390fd',
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
        }

class ProcedureUpdateReqBody(BaseModel):
    name: str | None = None
    version: str | None = None
    description: str | None = None
    checks: list[UUID] | None = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'some_fancy_name',
                'version': '0.0.1',
                'description': 'The scope of this procedure is defined by some theory about how to validate related data.',
                'checks': [
                    'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                    '00d31962-d426-4bde-86bd-1682b2a3d582'
                ]
            }
        }

class ProcedureResBody(BaseModel):
    id: UUID
    name: str
    version: str
    released: datetime | None = None
    description: str
    checks: list[UUID]

    links: list[Link] = []

    class Config:
        schema_extra = {
            'example': {
                'id': 'dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                'name': 'sum_is_zero',
                'version': '0.0.1',
                'released': '2022-08-25T19:50:12.352719',
                'description': 'The scope of this procedure is defined by some theory about how to validate related data.',
                'links': [
                    {
                        'href': '/procedures/dbf2a72a-15cf-4fc6-a7fd-879f75989a6c',
                        'rel': 'self',
                        'method': 'GET'
                    },
                    {
                        'href': '/procedures/dbf2a72a-15cf-4fc6-a7fd-879f75989a6c/checks',
                        'rel': 'checks',
                        'method': 'GET'
                    }
                ]
            }
        }

class ProcedureListResBody(BaseModel):
    procedures: list[Procedure] = []
    links: list[Link] = []
