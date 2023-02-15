import aiohttp
import asyncio
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name
from repositories.product import insert_product_data
from commons.backblaze import upload_image
import cloudscraper 
import cfscrape 

async def main():
    async with aiohttp.ClientSession() as session:
      brand = await get_brand_by_name('Laphroaig')
      url = 'https://www.thewhiskyexchange.com/search?q=%s' % ('Laphroaig')

      scraper = cfscrape.create_scraper() 
      content = scraper.get(url).text
      #scraper = cloudscraper.create_scraper(delay=10, browser="chrome") 
      #content = scraper.get(url).text 
      print(content)
      #res = await fetch_get(we_headers, session, url)
      #print(res)
      soup = BeautifulSoup(content, "lxml")
      products = []
      for prd in soup.find_all('li', {'class':'product-grid__item'}):
        products.append({
          'site': 'we',
          'brand_id': brand['_id'],
          'name': prd.find('a', {'class':'product-card'})['title'],
          'img': upload_image(prd.find('img', {'class':'product-card__image'})['src'], 'we'),
          'link': 'https://www.thewhiskyexchange.com' + prd.find('a', {'class':'product-card'})['href'],
          'price': prd.find('p', {'class':'product-card__price'}).text.strip()
        })
      print(products)
      #await insert_product_data(products)
      