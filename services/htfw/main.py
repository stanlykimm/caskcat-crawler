import aiohttp
import asyncio
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name
from repositories.product import insert_product_data

async def main():
    async with aiohttp.ClientSession() as session:
      brand = await get_brand_by_name('Laphroaig')

      url = 'https://www.htfw.com/catalogsearch/result/?q=%s&product_list_limit=80' % ('Laphroaig')
      res = await fetch_get(htfw_headers, session, url)
      soup = BeautifulSoup(res, "lxml")

      products = []
      idx = 0
      for prd in soup.find_all('li', {'class':'item product product-item'}):
        idx = idx + 1
        products.append({
          'site': 'htfw',
          'brand_id': brand['_id'],
          'description': prd.find('div', {'class':'product-item-description'}).text.strip(),
          'name': prd.find('span', {'class':'product-image-wrapper'}).find('img')['alt'],
          'img': prd.find('span', {'class':'product-image-wrapper'}).find('img')['src'],
          'link': prd.find('a', {'class':'product photo product-item-photo'})['href'],
          'price': prd.find('span', {'class':'price-wrapper'}).text.strip()
        })

      await insert_product_data(products)
      print(products)
