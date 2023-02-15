import aiohttp
import asyncio
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name, get_brands
from repositories.product import insert_product_data, get_products_by_site
from commons.backblaze import upload_image

async def main():
    async with aiohttp.ClientSession() as session:
      #brand = await get_brand_by_name('Laphroaig')
      brands = await get_brands()
      stored_products = await get_products_by_site('htfw')

      barnd_index = 0
      for brand in brands:
        barnd_index = barnd_index + 1
        print(barnd_index, brand.name_eng)
        url = 'https://www.htfw.com/catalogsearch/result/?q=%s&product_list_limit=80' % (brand.name_eng)
        print(url)
        res = await fetch_get(htfw_headers, session, url)
        soup = BeautifulSoup(res, "lxml")

        products = []
        idx = 0
        for prd in soup.find_all('li', {'class':'item product product-item'}):
          #print(prd)
          def check_data(product_id):
            for sp in stored_products:
              if 'product_id' in sp and product_id == sp['product_id']:
                return True
          
          try:
            product_id = prd.find('input', {'name': 'product'})['value']
          except TypeError as e:
            product_id = None
          
          if product_id is None or check_data(prd.find('input', {'name': 'product'})['value']) == True:
            continue

          idx = idx + 1
          products.append({
            'site': 'htfw',
            'brand_id': str(brand.id),
            'product_id': prd.find('input', {'name': 'product'})['value'],
            'description': prd.find('div', {'class':'product-item-description'}).text.strip(),
            'name': prd.find('span', {'class':'product-image-wrapper'}).find('img')['alt'],
            'img': upload_image(prd.find('span', {'class':'product-image-wrapper'}).find('img')['data-original'], 'htfw'),
            'link': prd.find('a', {'class':'product photo product-item-photo'})['href'],
            'price': prd.find('span', {'class':'price-wrapper'}).text.strip()
          })

        if len(products) == 0:
          print('products is empty')
        else:
          await insert_product_data(products) 
        #print(products)
