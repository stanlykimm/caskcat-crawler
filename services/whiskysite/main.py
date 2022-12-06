import json
import aiohttp
import asyncio
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name
from repositories.product import insert_product_data


async def main():
    async with aiohttp.ClientSession() as session:
      brand = await get_brand_by_name('Laphroaig')

      url = 'https://www.whiskysite.nl/en/search/%s/?format=json' % ('Laphroaig')
      res = await fetch_get(whiskysite_headers, session, url)
      data = json.loads(res)

      products = []
      res_products = data['collection']['products']
      for product_id in res_products:
        img = 'https://static.webshopapp.com/shops/039103/files/%s/325x375x2/image.jpg' % (res_products[product_id]['image'])
        products.append({
          'site': 'whiskysite',
          'brand_id': brand['_id'],
          'country': res_products[product_id]['brand']['title'],
          'distillery': res_products[product_id]['sku'],
          'description': res_products[product_id]['description'],
          'name': res_products[product_id]['title'],
          'img': img,
          'link': res_products[product_id]['url'],
          'price': res_products[product_id]['price']['price'],
        })
      await insert_product_data(products)
      print(products)
