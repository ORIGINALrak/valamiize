from fastapi import APIRouter, HTTPException, status

from server.models.procedure import ProcedureReqBody, ProcedureUpdateReqBody, Procedure
from uuid import UUID
from datetime import datetime


router = APIRouter()


# TODO: when using db think about how to handle if only some 'checks' modification is requested


# We do not use real database yet.
temp_procedures_db = []



@router.post('/',
             status_code=status.HTTP_201_CREATED,
             description=''
             )
async def create_procedure(input_procedure: ProcedureReqBody) -> Procedure:
    for procedure in temp_procedures_db:
        if procedure.uuid == input_procedure.uuid:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Procedure already exists.'
                )

    input_data = Procedure(**input_procedure.dict(exclude_unset=True), released=datetime.now())
    temp_procedures_db.append(input_data)

    return input_data



@router.get('/',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def read_procedures() -> list[Procedure]:
    return temp_procedures_db



@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def read_procedure(id: UUID) -> Procedure:
    for procedure in temp_procedures_db:
        if procedure.uuid == id:
            return procedure
    
    raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail='Procedure does not exists.'
                )



@router.put('/{id}',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def update_procedure(id: UUID, input_procedure: ProcedureUpdateReqBody) -> Procedure:
    i = 0
    for procedure in temp_procedures_db:
        if procedure.uuid == id:
            update_data = input_procedure.dict(exclude_unset=True)
            updated_procedure = procedure.copy(update=update_data)
            temp_procedures_db[i] = updated_procedure
            return updated_procedure
        
        i += 1
    
    raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail='Procedure does not exists.'
                )



@router.delete('/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description=''
               )
async def delete_procedure(id: UUID) -> None:
    i = 0
    for procedure in temp_procedures_db:
        if procedure.uuid == id:
            del temp_procedures_db[i]
            return
        
        i += 1
    
    raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail='Procedure does not exists.'
                )