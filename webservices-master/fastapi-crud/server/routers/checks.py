from fastapi import APIRouter, HTTPException, status

from server.models.check import CheckReqBody, CheckUpdateReqBody, Check
from uuid import UUID
from datetime import datetime


router = APIRouter()


# TODO: Body & Path parameters description
# TODO: endpoint description
# TODO: route title and description in app.py?
# TODO: update_check - get uuid from path paramater and do not update from body



# We do not use real database yet.
temp_checks_db = []



@router.post('/',
             status_code=status.HTTP_201_CREATED,
             description=''
             )
async def create_check(input_check: CheckReqBody) -> Check:
    for check in temp_checks_db:
        if check.uuid == input_check.uuid:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Check already exists.'
                )
    input_data = Check(**input_check.dict(exclude_unset=True), released=datetime.now())
    temp_checks_db.append(input_data)
    return input_data



@router.get('/',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def read_checks() -> list[Check]:
    return temp_checks_db



@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def read_check(id: UUID) -> Check:
    for check in temp_checks_db:
        if check.uuid == id:
            return check
    
    raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail='Check does not exists.'
                )



@router.put('/{id}',
            status_code=status.HTTP_200_OK,
            description=''
            )
async def update_check(id: UUID, input_check: CheckUpdateReqBody) -> Check:
    i = 0
    for check in temp_checks_db:
        if check.uuid == id:
            update_data = input_check.dict(exclude_unset=True)
            updated_item = check.copy(update=update_data)
            temp_checks_db[i] = updated_item
            return updated_item
        
        i += 1
    
    raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail='Check does not exists.'
                )



@router.delete('/{id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description=''
               )
async def delete_check(id: UUID) -> None:
    i = 0
    for check in temp_checks_db:
        if check.uuid == id:
            del temp_checks_db[i]
            return
        
        i += 1
    
    raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail='Check does not exists.'
                )