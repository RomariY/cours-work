from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Request, Query
from fastapi.encoders import jsonable_encoder
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.libraries import schemas
from api.libraries.filters import LibraryFilter
from api.libraries.models import Library

router = APIRouter(
    prefix="/library",
    tags=["library"],
    responses={
        200: {"description": "Successful Response"},
        404: {"description": "The page not found"}
    },
)
crud = CrudBase(Library)


@router.get("/", response_model=List[schemas.LibrarySchema])
async def list_construction(
        request: Request,
        name: Union[str, None] = Query(default="", max_length=50),
        type_filter: Union[str, None] = Query(default="", max_length=50),
):
    filter_kwargs = {
        "name": name,
        "type": type_filter
    }
    response_json = LibraryFilter(filter_kwargs).apply(Library)
    obj = list(response_json.dicts())
    return JSONResponse(status_code=status.HTTP_200_OK, content=obj)


@router.get("/{pk}", response_model=List[schemas.LibrarySchema])
async def retrieve_construction(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/",
    response_model=schemas.LibrarySchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_construction(item: schemas.LibraryCreateSchema, request: Request):
    kwargs = item.dict()
    obj = crud.create_obj(**kwargs)
    # Change UUID to str
    obj['id'] = str(obj['id'])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)


@router.patch(
    "/{pk}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.LibrarySchema,
)
async def update_construction(pk: UUID, item: schemas.LibraryUpdateSchema, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    updated_data = item.dict(exclude_none=True)
    schema_data = schemas.LibraryUpdateSchema.parse_obj(updated_data)
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
