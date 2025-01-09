from uuid import UUID
from db.session import Base, engine
from sqlalchemy import Table, Column, ForeignKey, String, TIMESTAMP, text, ARRAY
from sqlalchemy.dialects.postgresql import UUID



class Check(Base):
    __tablename__ = 'checks'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    released = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    description = Column(String, nullable=False)
    lang = Column(String, nullable=False)
    params = Column(ARRAY(String), nullable=True)
    func_body = Column(String, nullable=False)


class Procedure(Base):
    __tablename__ = 'procedures'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    released = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    description = Column(String, nullable=False)

    checks = Column(ARRAY(UUID(as_uuid=True)), nullable=True)