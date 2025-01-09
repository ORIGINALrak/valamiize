from fastapi import APIRouter, HTTPException, status, Depends
from starlette.requests import Request
from pymongo.errors import DuplicateKeyError

from db.session import init_db
from db.models import Check, Procedure
from schemas.check import CheckCreateReqBody, CheckUpdateReqBody, CheckResBody, CheckListResBody
from schemas.procedure import ProcedureListResBody
from schemas.link import Link

from uuid import UUID
from datetime import datetime


# TODO: write pipeline for querying {id}/procedures
# TODO: write aggregation pipeline which updates procedure if a check is deleted
# TODO: HATEOAS links


router = APIRouter()


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             description='',
             response_model=Check
             )
async def create_check(input_check: CheckCreateReqBody) -> Check:
    db_check = Check(**input_check.dict(), released=datetime.now())
    try:
        await db_check.create()
    except DuplicateKeyError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Check already exists.'
            )
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    new_check = await Check.get(db_check.id)
    return new_check


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=CheckResBody
            )
async def read_check(request: Request, id: UUID) -> CheckResBody:
    db_check = await Check.get(id)
    
    if not db_check:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Check does not exists.'
            )
            
    response_check = CheckResBody(
        **db_check.dict(),
        links=[
            Link(href=f'{request.url.path}', rel='self', method='GET'),
            Link(href=f'{request.url.path}/procedures', rel='procedures', method='GET')
        ])

    return response_check


@router.get('/',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=CheckListResBody
            )
async def read_checks(request: Request, skip: int = 0, limit: int =10) -> CheckListResBody:
    db_checks = await Check.find_all().skip(skip).limit(limit).to_list()

    response_links = [
        Link(href=f'{request.url.path}', rel='self', method='GET')
    ]

    for db_check in db_checks:
        response_links.append(
            Link(href=f'{request.url.path}{db_check.id}', rel='single_check', method='GET')
            )

    response = CheckListResBody(checks=db_checks, links=response_links)
    return response


@router.get('/{id}/procedures',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def read_check_procedures(request: Request, id: UUID) -> dict:
    return {'not': 'implemented yet.'}




@router.put('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=Check
            )
async def update_check(id: UUID, input_check: CheckUpdateReqBody) -> Check:
    db_check = await Check.get(id)
    
    if not db_check:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Check does not exists.'
            )
    
    await db_check.set(input_check.dict(exclude_none=True))
    
    return db_check



@router.delete('/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description=''
               )
async def delete_check(id: UUID) -> None:
    db_check = await Check.get(id)

    if not db_check:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Check does not exists.'
            )
    
    await db_check.delete()

    return