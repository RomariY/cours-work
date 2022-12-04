from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Request, Query
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.operators import schemas
from api.operators.filters import OperatorFilter
from api.operators.models import Operator

router = APIRouter(
    prefix="/operator",
    tags=["operator"],
    responses={
        200: {"description": "Successful Response"},
        404: {"description": "The page not found"}
    },
)
crud = CrudBase(Operator)


@router.get("/", response_model=List[schemas.OperatorSchema])
async def list_construction(
        request: Request,
        name: Union[str, None] = Query(default="", max_length=50),
):
    filter_kwargs = {
        "name": name,
    }
    response_json = OperatorFilter(filter_kwargs).apply(Operator)
    obj = list(response_json.dicts())
    return JSONResponse(status_code=status.HTTP_200_OK, content=obj)


@router.get("/{pk}", response_model=List[schemas.OperatorSchema])
async def retrieve_construction(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/",
    response_model=schemas.OperatorSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_construction(item: schemas.OperatorCreateSchema, request: Request):
    kwargs = item.dict()
    obj = crud.create_obj(**kwargs)
    # Change UUID to str
    obj['id'] = str(obj['id'])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)


@router.patch(
    "/{pk}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.OperatorSchema,
)
async def update_construction(pk: UUID, item: schemas.OperatorUpdateSchema, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    updated_data = item.dict(exclude_none=True)

    for key in updated_data.keys():
        try:
            tp = type(updated_data[key]).__name__
            if tp == "str" or tp == "UUID":
                exec(f'obj.{key} = {tp}("{updated_data[key]}")')
            else:
                exec(f'obj.{key} = {tp}({updated_data[key]})')
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
    return {"status_code": 204, "message": "Successfully deleted"}
