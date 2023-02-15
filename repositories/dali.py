from datetime import datetime

from pymongo.cursor import Cursor
from models.mongodb import mongodb

async def get_all_products():
    """전체 데이터 가져오기"""
    cursor: Cursor = mongodb.dali.find({})
    return [dict(**doc) async for doc in cursor]


async def update_prouct(product: dict):
    """위스키 상품 데이터 입력"""
    cursor: Cursor = await mongodb.dali.update_one({"_id":product['id']}, {"$set":{"caskcat_url":product['url']}})
