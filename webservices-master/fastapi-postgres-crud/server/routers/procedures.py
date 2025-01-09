from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.procedure import ProcedureReqBody, ProcedureUpdateReqBody, ProcedureInDB
from crud import crud_procedures

from uuid import UUID
from datetime import datetime


# TODO: Body, Path, Query parameters description
# TODO: endpoint description



router = APIRouter()


@router.get('/',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=list[ProcedureInDB]
            )
async def read_procedures(skip: int = 0, limit: int =10, db: Session = Depends(get_db)) -> list[ProcedureInDB]:
    return crud_procedures.get_procedures(db=db, skip=skip, limit=limit)


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=ProcedureInDB
            )
async def read_procedure(id: UUID, db: Session = Depends(get_db)) -> ProcedureInDB:
    db_procedure = crud_procedures.get_procedure_by_id(db=db, id=id)
    
    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )
    
    return db_procedure


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             description='',
             response_model=ProcedureInDB
             )
async def create_procedure(input_procedure: ProcedureReqBody, db: Session = Depends(get_db)) -> ProcedureInDB:
    db_procedure = crud_procedures.get_procedure_by_id(db=db, id=input_procedure.id)
    if db_procedure:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Procedure already exists.'
            )

    return crud_procedures.create_procedure(db=db, procedure_req=input_procedure)


@router.put('/{id}',
            status_code=status.HTTP_200_OK,
            description='',
            response_model=ProcedureInDB
            )
async def update_procedure(id: UUID, input_procedure: ProcedureUpdateReqBody, db: Session = Depends(get_db)) -> ProcedureInDB:
    db_procedure = crud_procedures.get_procedure_by_id(db=db, id=id)

    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )

    return crud_procedures.update_procedure_by_id(db=db, id=id, procedure_update_req=input_procedure)


@router.delete('/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description=''
               )
async def delete_procedure(id: UUID, db: Session = Depends(get_db)) -> None:
    db_procedure = crud_procedures.get_procedure_by_id(db=db, id=id)

    if not db_procedure:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Procedure does not exists.'
            )
    
    return crud_procedures.remove_procedure(db=db, id=id)