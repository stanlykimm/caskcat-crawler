import time
import logging
import random
import secrets
import aiohttp
import asyncio
import json
import os
import requests
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from commons.backblaze import upload_file, b2
from repositories.dali import get_all_products, update_prouct

logging.basicConfig(level=logging.INFO)
host = 'https://f004.backblazeb2.com/file/caskcat'

async def main():
  for row in await get_all_products():
    name = str(secrets.token_hex(nbytes=32))
    r = requests.get(row['image_src'], stream=True)
    with open(name, 'wb') as f:
        for chunk in r:
            f.write(chunk)
    rtn = upload_file('caskcat', '', name,  b2, 'dali/'+name)
    os.remove(name)

    url = host + '/' + 'dali/' + name

    await update_prouct({'id': row['_id'], 'url': url})
    print(url)