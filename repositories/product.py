from datetime import datetime

from pymongo.cursor import Cursor
from models.mongodb import mongodb


async def insert_product_data(products: list):
    """위스키 상품 데이터 입력"""
    cursor: Cursor = await mongodb.product.insert_many(products)


async def get_products_by_site(site: str):
    """위스키 브랜드 이름으로 검색하기"""
    cursor: Cursor = mongodb.product.find({
        'site': site
    })
    return [dict(**doc) async for doc in cursor]


async def get_all_products():
    cursor: Cursor = mongodb.product.find({})
    return [dict(**doc) async for doc in cursor]


async def update_prouct(_id, product: dict):
    cursor: Cursor = await mongodb.product.update_one({"_id":_id}, {"$set":product})
