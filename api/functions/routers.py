from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Request, Query
from playhouse.shortcuts import model_to_dict
from starlette import status
from starlette.responses import JSONResponse

from api.base.crud import CrudBase
from api.functions import schemas
from api.functions.filters import DataTypeFilter, FunctionFilter
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
async def list_data_type(
        request: Request,
        name: Union[str, None] = Query(default="", max_length=50)
):
    filter_kwargs = {
        "name": name
    }
    obj = list(DataTypeFilter(filter_kwargs).apply(DataType).dicts())
    return JSONResponse(status_code=status.HTTP_200_OK, content=obj)


@router.get("/data-type/{pk}", response_model=List[schemas.DataTypeSchema])
async def retrieve_data_type(pk: UUID, request: Request):
    obj = data_type_crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.patch(
    "/data-type/{pk}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.DataTypeSchema,
)
async def update_data_type(pk: UUID, item: schemas.DataTypeCreateSchema, request: Request):
    obj = data_type_crud.get_obj(pk)
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


@router.post(
    "/data-type-create",
    response_model=schemas.DataTypeSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_data_type(item: schemas.DataTypeCreateSchema, request: Request):
    kwargs = item.dict()
    obj = data_type_crud.create_obj(**kwargs)
    response = serialize_dict(obj)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)


@router.delete(
    "/data-type/{pk}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_data_type(pk: UUID, request: Request):
    obj = data_type_crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    data_type_crud.delete_obj(pk)
    return None


# Functions endpoints
@router.get("/", response_model=List[schemas.FunctionSchema])
async def list_function(
        request: Request,
        name: Union[str, None] = Query(default="", max_length=50),
        data_type: Union[str, None] = Query(default="", max_length=50)

):
    filter_kwargs = {
        "name": name,
    }

    response_json = FunctionFilter(filter_kwargs).apply(Function)
    if data_type:
        response_json = response_json.join(DataType).where(DataType.name == data_type)
    obj = list(response_json.dicts())
    for each in obj:
        data_type = each.get("return_type")
        data_type_obj = data_type_crud.get_obj(data_type)
        each.update({"return_type": model_to_dict(data_type_obj)})
    return JSONResponse(status_code=status.HTTP_200_OK, content=obj)


@router.get("/{pk}", response_model=List[schemas.FunctionSchema])
async def retrieve_function(pk: UUID, request: Request):
    obj = model_to_dict(crud.get_obj(pk))
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=model_to_dict(obj))


@router.post(
    "/",
    response_model=schemas.FunctionSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_function(item: schemas.FunctionCreateSchema, request: Request):
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
async def update_function(pk: UUID, item: schemas.FunctionCreateSchema, request: Request):
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
async def delete_function(pk: UUID, request: Request):
    obj = crud.get_obj(pk)
    if not obj:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    crud.delete_obj(pk)
    return None
