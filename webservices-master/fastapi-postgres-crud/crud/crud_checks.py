from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from db.models import Check
from schemas import check


def get_checks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Check).offset(skip).limit(limit).all()

def get_check_by_id(db: Session, id = UUID):
    return db.query(Check).filter(Check.id == id).first()

def create_check(db: Session, check_req=check.CheckReqBody):
    db_check = Check(**check_req.dict())
    db.add(db_check)
    db.commit()
    db.refresh(db_check)

    return db_check

def update_check_by_id(db: Session, id: UUID, check_update_req=check.CheckUpdateReqBody):
    check_query = db.query(Check).filter(Check.id == id)
    check_query.update(check_update_req.dict(exclude_unset=True), synchronize_session=False)
    db.commit()

    return check_query.first()

def remove_check(db: Session, id: UUID):
    db_check = get_check_by_id(db=db, id=id)
    db.delete(db_check)
    db.commit()