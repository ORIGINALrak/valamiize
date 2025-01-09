from uuid import UUID
from sqlalchemy.orm import Session

from db.models import Procedure
from schemas import procedure


def get_procedures(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Procedure).offset(skip).limit(limit).all()

def get_procedure_by_id(db: Session, id = UUID):
    return db.query(Procedure).filter(Procedure.id == id).first()

def create_procedure(db: Session, procedure_req=procedure.ProcedureReqBody):
    db_procedure = Procedure(**procedure_req.dict())
    db.add(db_procedure)
    db.commit()
    db.refresh(db_procedure)

    return db_procedure

def update_procedure_by_id(db: Session, id: UUID, procedure_update_req=procedure.ProcedureUpdateReqBody):
    procedure_query = db.query(Procedure).filter(Procedure.id == id)
    procedure_query.update(procedure_update_req.dict(exclude_unset=True), synchronize_session=False)
    db.commit()

    return procedure_query.first()

def remove_procedure(db: Session, id: UUID):
    db_procedure = get_procedure_by_id(db=db, id=id)
    db.delete(db_procedure)
    db.commit()