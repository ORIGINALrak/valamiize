from pydantic import BaseModel


class Link(BaseModel):
    href: str
    rel: str
    method: str

    class Config:
        schema_extra = {
            'example': {
                'href': '/checks/dbf2a72a-15cf-4fc6-a7fd-879f75989a6c/procedures',
                'rel': 'procedures',
                'method': 'GET'
            }
        }