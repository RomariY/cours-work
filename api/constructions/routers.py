from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Request, Query
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.constructions import schemas
from api.constructions.filters import ConstructionFilter
from api.constructions.models import Construction

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
async def list_construction(
        request: Request,
        name: Union[str, None] = Query(default="", max_length=50)
):
    filter_kwargs = {
        "name": name
    }
    obj = list(ConstructionFilter(filter_kwargs).apply(Construction).dicts())
    return JSONResponse(status_code=status.HTTP_200_OK, content=obj)


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
    # Change UUID to str
    obj['id'] = str(obj['id'])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)


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
    return {"status_code": 204, "message": "Successfully deleted"}
