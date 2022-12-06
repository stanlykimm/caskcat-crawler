from datetime import datetime

from pymongo.cursor import Cursor
from models.mongodb import mongodb


async def insert_product_data(products: list):
    """위스키 상품 데이터 입력"""
    cursor: Cursor = await mongodb.product.insert_many(products)