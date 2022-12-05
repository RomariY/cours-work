from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Request, Query
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.glossary import schemas
from api.glossary.filters import GlossaryFilter
from api.glossary.models import Glossary

router = APIRouter(
    prefix="/glossary",
    tags=["glossary"],
    responses={
        200: {"description": "Successful Response"},
        404: {"description": "The page not found"}
    },
)
crud = CrudBase(Glossary)


@router.get("/", response_model=List[schemas.GlossarySchema])
async def list_construction(
        request: Request,
        name: Union[str, None] = Query(default="", max_length=50),
):
    filter_kwargs = {
        "name": name,
    }
    response_json = GlossaryFilter(filter_kwargs).apply(Glossary)
    obj = list(response_json.dicts())
    return JSONResponse(status_code=status.HTTP_200_OK, content=obj)


@router.get("/{pk}", response_model=List[schemas.GlossarySchema])
async def retrieve_construction(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/",
    response_model=schemas.GlossarySchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_construction(item: schemas.GlossaryCreateSchema, request: Request):
    kwargs = item.dict()
    obj = crud.create_obj(**kwargs)
    # Change UUID to str
    obj['id'] = str(obj['id'])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)


@router.patch(
    "/{pk}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.GlossarySchema,
)
async def update_construction(pk: UUID, item: schemas.GlossaryUpdateSchema, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    updated_data = item.dict(exclude_none=True)
    schema_data = item.parse_obj(updated_data)
    for each in schema_data:
        key = each[0]
        try:
            exec(f'obj.{key} = schema_data.{key}')
        except ValueError:
            raise ValueError(f"Failed to assign {updated_data[key]} field to {key}")
    obj.save()
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.delete(
    "/{pk}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_construction(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    crud.delete_obj(pk)
    return None
