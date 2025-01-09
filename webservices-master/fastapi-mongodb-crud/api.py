from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from db.session import init_db
from routers import checks, procedures


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

@app.on_event("startup")
async def start_db():
    await init_db()