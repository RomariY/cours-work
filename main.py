from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from api.base import database
from api.constructions import routers as constructors


app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(constructors.router)
