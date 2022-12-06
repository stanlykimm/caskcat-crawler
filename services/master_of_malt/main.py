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
      brand = await get_brand_by_name('Bowmore')

      url = 'https://www.masterofmalt.com/api/appsearch/search/?currencyid=27&deliverycountryid=352&tradegroupid=0&ext=.json'
      mom_query_data['query'] = 'Bowmore'
      res = await fetch_post(mom_headers, session, url, mom_query_data)
      dataset = json.loads(res)
      
      products = []
      for r in dataset['results']:
        products.append({
          'site': 'mom',
          'brand_id': brand['_id'],
          'country': r['country']['raw'],
          'distillery': r['distillery']['raw'],
          'description': r['description']['raw'],
          'bottler': r['country']['raw'],
          'name': r['title']['raw'],
          'img': r['productimage']['raw'],
          'link': r['url']['raw'],
          'price': r['price']['raw']
        })
      await insert_product_data(products)
      print(products)


