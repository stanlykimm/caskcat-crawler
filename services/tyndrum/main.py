import json
import aiohttp
import asyncio
import traceback
import time
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name, get_brands
from repositories.product import insert_product_data, get_products_by_site
from commons.backblaze import upload_image

async def main():
    async with aiohttp.ClientSession() as session:
      brands = await get_brands()
      stored_products = await get_products_by_site('tyndrum')

      brand_index = 0 
      for brand in brands:
        time.sleep(40)
        brand_index = brand_index + 1
        print(brand_index, brand.name_eng)

        url = 'https://www.tyndrumwhisky.com/catalogsearch/result/?q=%s' % (brand.name_eng)
        print(url)
        res = await fetch_get(tyndrum_headers, session, url)
        soup = BeautifulSoup(res, "lxml")

        products = []
        for prd in soup.find_all('li', attrs={'class':'item product product-item'}):
          prd_info = prd.find('div', attrs={'class': 'product details product-item-details'})
          prd_img = prd.find('div', attrs={'class': 'product_image'})
          product_id = prd_info.find('div', attrs={'class': 'price-box price-final_price'})['data-product-id']
          print(product_id)
          def check_data(product_id):
            for sp in stored_products:
              if 'product_id' in sp and product_id == sp['product_id']:
                return True
          
          if check_data(product_id) == True:
            continue

          img_url = prd_img.find('img', attrs={'class': 'product-image-photo'})['src']
          print(img_url)

          products.append({
            'site': 'tyndrum',
            'product_id': prd_info.find('div', attrs={'class': 'price-box price-final_price'})['data-product-id'],
            'name': prd_info.find('a', attrs={'class': 'product-item-link'}).text.strip(),
            'img': upload_image(img_url, 'tyndrum'),
            'link': prd_info.find('a', attrs={'class': 'product-item-link'})['href'],
            'price': prd_info.find('span', attrs={'class': 'price'}).text.strip().replace('Â£', '')
          })
        if len(products) == 0:
          print('products is empty')
        else:
          await insert_product_data(products)      

