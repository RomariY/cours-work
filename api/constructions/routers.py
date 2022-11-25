from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.constructions import schemas
from api.constructions.models import Construction
from utils.utils import serialize_dict

router = APIRouter(
    prefix="/constructions",
    tags=["constructions"],
    responses={
        200: {"description": "Successful Response"},
        204: {"description": "No content"},
        404: {"description": "The page not found"}
    },
)
crud = CrudBase(Construction)


@router.get("/", response_model=List[schemas.ConstructionSchema])
async def list_construction(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content=crud.get_objs())


@router.get("/{pk}", response_model=List[schemas.ConstructionSchema])
async def retrieve_construction(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/",
    response_model=schemas.ConstructionSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_construction(item: schemas.ConstructionCreateSchema, request: Request):
    kwargs = item.dict()
    obj = crud.create_obj(**kwargs)
    response = serialize_dict(obj)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)


@router.patch(
    "/{pk}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ConstructionSchema,
)
async def update_construction(pk: UUID, item: schemas.ConstructionUpdateSchema, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    updated_data = item.dict(exclude_none=True)
    for key in updated_data.keys():
        exec(f"obj.{key} = '{updated_data[key]}'")
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
