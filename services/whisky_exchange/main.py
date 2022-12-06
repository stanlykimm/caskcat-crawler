import aiohttp
import asyncio
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name
from repositories.product import insert_product_data
import cfscrape


async def main():
    async with aiohttp.ClientSession() as session:
      brand = await get_brand_by_name('Laphroaig')
      url = 'https://www.thewhiskyexchange.com/search?q=%s' % ('Laphroaig')
      print(url)
      res = await fetch_get(we_headers, session, url)
      print(res)
      soup = BeautifulSoup(res, "lxml")
      products = []
      for prd in soup.find_all('li', {'class':'product-grid__item'}):
        products.append({
          'site': 'we',
          'brand_id': brand['_id'],
          'name': prd.find('a', {'class':'product-card'})['title'],
          'img': prd.find('img', {'class':'product-card__image'})['src'],
          'link': prd.find('a', {'class':'product-card'})['href'],
          'price': prd.find('p', {'class':'product-card__price'}).text.strip()
        })
      print(products)
      await insert_product_data(products)
      