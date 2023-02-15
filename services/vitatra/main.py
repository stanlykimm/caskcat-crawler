from commons.utils import *
from commons.brand import *
from commons.data import *
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from repositories.brand import get_brand_by_name
from repositories.product import insert_product_data
from commons.backblaze import upload_image


async def main():
    async with aiohttp.ClientSession() as session:
      url = 'https://www.vitatra.de/product/category/689-690/page/0?orderby=인기순'

      res = await fetch_get(vitatra_headers, session, url)
      soup = BeautifulSoup(res, "lxml")
      products = []
      for prd in soup.find(id='category_list').find_all('td'):
        products.append({
          'site': 'vitatra',
          'img':  upload_image('https://www.vitatra.de' + prd.find('div', {'class':'img'}).find('img')['src'], 'vitatra'),
          'link': 'https://www.vitatra.de' + prd.find('a', {'class':'item_list_name'})['href'],
          'brand': prd.find('span', {'class':'cmp'}).text.strip(),
          'name': prd.find('a', {'class':'item_list_name'}).text.strip(),
          'price': prd.find('p', {'class':'price'}).text.strip(),

        })
      print(products)


