from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.functions import schemas
from api.functions.models import Function, DataType
from utils.utils import serialize_dict, check_pk_exist

router = APIRouter(
    prefix="/functions",
    tags=["functions"],
    responses={
        200: {"description": "Successful Response"},
        404: {"description": "The page not found"}
    },
)
data_type_crud = CrudBase(DataType)
crud = CrudBase(Function)


# DataType endpoints
@router.get("/data-type", response_model=List[schemas.DataTypeSchema])
async def list_construction(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content=data_type_crud.get_objs())


@router.get("/data-type/{pk}", response_model=List[schemas.DataTypeSchema])
async def retrieve_construction(pk: UUID, request: Request):
    obj = data_type_crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/data-type-create",
    response_model=schemas.DataTypeSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_construction(item: schemas.DataTypeCreateSchema, request: Request):
    kwargs = item.dict()
    obj = data_type_crud.create_obj(**kwargs)
    response = serialize_dict(obj)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)


# Functions endpoints
@router.get("/", response_model=List[schemas.FunctionSchema])
async def list_construction(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content=crud.get_objs())


@router.get("/{pk}", response_model=List[schemas.FunctionSchema])
async def retrieve_construction(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/",
    response_model=schemas.FunctionSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_construction(item: schemas.FunctionCreateSchema, request: Request):
    kwargs = item.dict()
    data_type_pk = kwargs.get("return_type")
    exist_status = check_pk_exist(DataType, data_type_pk)
    if not exist_status:
        return JSONResponse(status_code=404, content={"message": "DataType with this UUID doesn't exist"})
    obj = crud.create_obj(**kwargs)
    # Change UUID to str
    obj['id'] = str(obj['id'])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)


@router.patch(
    "/{pk}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.FunctionSchema,
)
async def update_construction(pk: UUID, item: schemas.FunctionCreateSchema, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    updated_data = item.dict(exclude_none=True)

    # Check DataType FK
    data_type_pk = updated_data.get("return_type")
    if data_type_pk:
        exist_status = check_pk_exist(DataType, data_type_pk)
        if not exist_status:
            return JSONResponse(status_code=404, content={"message": "DataType with this UUID doesn't exist"})
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
    return None
