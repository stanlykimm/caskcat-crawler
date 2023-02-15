import json
import aiohttp
import asyncio
import traceback
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name, get_brands
from repositories.product import insert_product_data, get_products_by_site
from commons.backblaze import upload_image

async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.tyndrumwhisky.com/catalogsearch/result/?q=%s' % ('Bowmore')
        res = await fetch_get(tyndrum_headers, session, url)
        soup = BeautifulSoup(res, "lxml")

        products = []
        for prd in soup.find_all('li', attrs={'class':'item product product-item'}):
          prd_info = prd.find('div', attrs={'class': 'product details product-item-details'})
          prd_img = prd.find('div', attrs={'class': 'product_image'})
          
          r = {
            'site': 'tyndrum',
            'product_id': prd_info.find('div', attrs={'class': 'price-box price-final_price'})['data-product-id'],
            'name': prd_info.find('a', attrs={'class': 'product-item-link'}).text.strip(),
            'img': prd_img.find('img', attrs={'class': 'product-image-photo'})['src'],
            'link': prd_info.find('a', attrs={'class': 'product-item-link'})['href'],
            'price': prd_info.find('span', attrs={'class': 'price'}).text.strip().replace('Â£', '')
          }
          print(r)

