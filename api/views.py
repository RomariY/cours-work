from multiprocessing import get_logger

from fastapi import Request, APIRouter

logger = get_logger()
router = APIRouter()


@router.get("/")
async def tester():
    return {"status": 200}


@router.get("/test/{item_id}")
async def tester(request: Request, item_id: int):
    return {"status": 200, "item_id": item_id}
