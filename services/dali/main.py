import aiohttp
import asyncio
import json
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name
from repositories.product import insert_product_data


async def main():
    async with aiohttp.ClientSession() as session:
      url = 'https://www.daligo.co.kr/controller/product/getGoodsList'

      data = {
        'page': '1',
        'max': '24',
        'filterCid': '002000000000000',
        'orderBy': 'orderCnt',
        'ForbizCsrfTestName': 'af3b9d16b0f7e98e8a1c0d7aa1b956c5'
      }

      res = await fetch_post(dali_headers, session, url, data)
      print(res)
      dataset = json.loads(res)
      print(dataset)





'''
curl 'https://www.daligo.co.kr/controller/product/getGoodsList' \
-X 'POST' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
-H 'Accept: */*' \
-H 'Accept-Language: en-GB,en;q=0.9' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Host: www.daligo.co.kr' \
-H 'Origin: https://www.daligo.co.kr' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15' \
-H 'Connection: keep-alive' \
-H 'Referer: https://www.daligo.co.kr/shop/goodsList/001000000000000' \
--data 'page=1&max=24&filterCid=001000000000000&orderBy=orderCnt&ForbizCsrfTestName=af3b9d16b0f7e98e8a1c0d7aa1b956c5'

'''


