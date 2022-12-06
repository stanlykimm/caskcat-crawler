from datetime import datetime

from pymongo.cursor import Cursor
from models.mongodb import mongodb


async def insert_product_data(product: dict):
    """위스키 상품 데이터 입력"""
    cursor: Cursor = await mongodb.dailyshot.insert_one(product)

async def get_row(idx: int):
    """위스키 브랜드 이름으로 검색하기"""
    cursor: Cursor = await mongodb.dailyshot.find_one({
        'product_id': idx
    })
    return cursor