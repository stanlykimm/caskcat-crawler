import json
import aiohttp
import asyncio
import traceback
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name, get_brands
from repositories.product import insert_product_data, get_products_by_site
from commons.backblaze import upload_image

async def main():
    async with aiohttp.ClientSession() as session:
      brands = await get_brands()
      stored_products = await get_products_by_site('whiskysite')

      idxx = 0
      for brand in brands:
        idxx = idxx + 1
        print(idxx, brand.name_eng)
        '''
        if idxx < 42:
          continue
        '''
        
        url = 'https://www.whiskysite.nl/en/search/%s/?format=json' % (brand.name_eng)
        res = await fetch_get(whiskysite_headers, session, url)
        data = json.loads(res)

        products = []
        res_products = data['collection']['products']
        if res_products is False:
          continue
        try:
          for product_id in res_products:
            def check_data(product_id):
              for sp in stored_products:
                if 'product_id' in sp and product_id == sp['product_id']:
                  return True
            
            if check_data(product_id) == True:
              continue
            
            img = 'https://static.webshopapp.com/shops/039103/files/%s/325x375x2/image.jpg' % (res_products[product_id]['image'])

            products.append({
              'site': 'whiskysite',
              'product_id': product_id,
              #'brand_id': brand['_id'],
              'distillery': res_products[product_id]['sku'],
              'description': res_products[product_id]['description'],
              'name': res_products[product_id]['title'],
              'img': upload_image(img, 'whiskysite'),
              'link': 'https://www.whiskysite.nl/' + res_products[product_id]['url'],
              'price': res_products[product_id]['price']['price'],
            })
        except TypeError as e:
          print(traceback.format_exc())
          print(data)
          print(res_products)
          
        if len(products) == 0:
          print('products is empty')
        else:
          await insert_product_data(products)          
        #print(products)
