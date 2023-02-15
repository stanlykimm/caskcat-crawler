from datetime import datetime

from pymongo.cursor import Cursor
from models.mongodb import mongodb
from models.collection import Brand

async def get_brand_by_name(brand_name: str) -> Brand:
    """위스키 브랜드 이름으로 검색하기"""
    cursor: Cursor = await mongodb.brand.find_one({
        'name_eng': brand_name
    })
    return cursor


async def get_brands():
  """위스키 브랜드 가져오기"""
  cursor: Cursor = mongodb.brand.find({})
  return [Brand(**doc) async for doc in cursor]