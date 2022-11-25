from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.constructions import routers as constructors
from api.functions import routers as functions
from api.glossary import routers as glossary
from api.libraries import routers as library
from api.operators import routers as operator

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
app.include_router(functions.router)
app.include_router(glossary.router)
app.include_router(library.router)
app.include_router(operator.router)
