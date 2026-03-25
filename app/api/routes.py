from fastapi import APIRouter
from app.services.data_service import get_heavy_data

router = APIRouter()

@router.get("/data")
async def fetch_data():
    result = await get_heavy_data()
    return result
