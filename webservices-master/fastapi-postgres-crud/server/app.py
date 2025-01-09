from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from .routers import home, checks, procedures
from db import session, models

session.Base.metadata.create_all(bind=session.engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    home.router,
    tags=['home']
    )
app.include_router(
    checks.router,
    prefix='/checks',
    tags=['checks']
    )
app.include_router(
    procedures.router,
    prefix='/procedures',
    tags=['procedures']
    )