from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from db.session import get_db
from schemas.check import CheckReqBody, CheckUpdateReqBody, CheckInDB
from crud import crud_checks

from uuid import UUID
from datetime import datetime


# TODO: Body, Path, Query parameters description
# TODO: endpoint description



router = APIRouter()


@router.get('/',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=list[CheckInDB]
            )
async def read_checks(skip: int = 0, limit: int =10, db: Session = Depends(get_db)) -> list[CheckInDB]:
    return crud_checks.get_checks(db=db, skip=skip, limit=limit)


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=CheckInDB
            )
async def read_check(id: UUID, db: Session = Depends(get_db)) -> CheckInDB:
    db_check = crud_checks.get_check_by_id(db=db, id=id)
    
    if not db_check:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Check does not exists.'
            )
    
    return db_check


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             description='',
             response_model=CheckInDB
             )
async def create_check(input_check: CheckReqBody, db: Session = Depends(get_db)) -> CheckInDB:
    db_check = crud_checks.get_check_by_id(db=db, id=input_check.id)
    if db_check:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Check already exists.'
            )

    return crud_checks.create_check(db=db, check_req=input_check)


@router.put('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=CheckInDB
            )
async def update_check(id: UUID, input_check: CheckUpdateReqBody, db: Session = Depends(get_db)) -> CheckInDB:
    db_check = crud_checks.get_check_by_id(db=db, id=id)

    if not db_check:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Check does not exists.'
            )

    return crud_checks.update_check_by_id(db=db, id=id, check_update_req=input_check)


@router.delete('/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description=''
               )
async def delete_check(id: UUID, db: Session = Depends(get_db)) -> None:
    db_check = crud_checks.get_check_by_id(db=db, id=id)

    if not db_check:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Check does not exists.'
            )
    
    return crud_checks.remove_check(db=db, id=id)