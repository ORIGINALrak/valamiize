from fastapi import APIRouter, HTTPException, status, Depends
from starlette.requests import Request
from pymongo.errors import DuplicateKeyError

from db.session import init_db
from db.models import Procedure, Check
from schemas.check import CheckListResBody
from schemas.procedure import ProcedureCreateReqBody, ProcedureUpdateReqBody, ProcedureResBody, ProcedureListResBody
from schemas.link import Link


from uuid import UUID
from datetime import datetime


router = APIRouter()


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             description='',
             response_model=Procedure
             )
async def create_procedure(input_procedure: ProcedureCreateReqBody) -> Procedure:
    db_procedure = Procedure(**input_procedure.dict(), released=datetime.now())
    try:
        await db_procedure.create()
    except DuplicateKeyError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Procedure already exists.'
            )
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    new_procedure = await Procedure.get(db_procedure.id)
    return new_procedure


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=ProcedureResBody
            )
async def read_procedure(request: Request, id: UUID) -> ProcedureResBody:
    db_procedure = await Procedure.get(id)
    
    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )
    
    response_procedure = ProcedureResBody(
        **db_procedure.dict(),
        links=[
            Link(href=f'{request.url.path}', rel='self', method='GET'),
            Link(href=f'{request.url.path}/checks', rel='checks', method='GET')
        ])

    return response_procedure


@router.get('/{id}/checks',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def read_procedure_checks(request: Request, id: UUID) -> dict:
    db_procedure = await Procedure.get(id)
    
    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )
    
    pipeline = [
        {
            '$match':
            {
                '_id': {'$in': [check for check in db_procedure.checks]}
            }
        }
    ]

    db_checks = await Check.find_all().aggregate(pipeline).to_list()

    response_links = [
        Link(href=f'{request.url.path}', rel='self', method='GET'),
        Link(href=request.url.path.removesuffix('/checks'), rel='parent_proc', method='GET')
    ]

    response = CheckListResBody(checks=db_checks, links=response_links)
    return response


@router.get('/',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=ProcedureListResBody
            )
async def read_procedures(request: Request, skip: int = 0, limit: int =10) -> ProcedureListResBody:
    db_procedures = await Procedure.find_all().skip(skip).limit(limit).to_list()

    response_links = [
        Link(href=f'{request.url.path}', rel='self', method='GET')
    ]

    for db_procedure in db_procedures:
        response_links.append(
            Link(href=f'{request.url.path}{db_procedure.id}', rel='single_procedure', method='GET')
            )

    response = ProcedureListResBody(procedures=db_procedures, links=response_links)
    return response


@router.put('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=Procedure
            )
async def update_procedure(id: UUID, input_procedure: ProcedureUpdateReqBody) -> Procedure:
    db_procedure = await Procedure.get(id)
    
    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )
    
    await db_procedure.set(input_procedure.dict(exclude_none=True))
    
    return db_procedure



@router.delete('/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description=''
               )
async def delete_procedure(id: UUID) -> None:
    db_procedure = await Procedure.get(id)

    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )
    
    await db_procedure.delete()

    return