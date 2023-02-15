import os
import aiohttp
import asyncio
import json
import secrets
import requests
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name, get_brands
from repositories.product import insert_product_data, get_products_by_site
from commons.backblaze import upload_file, b2, upload_image

host = 'https://f004.backblazeb2.com/file/caskcat'

async def main():
    async with aiohttp.ClientSession() as session:
      #brand = await get_brand_by_name('Bowmore')
      brands = await get_brands()
      stored_products = await get_products_by_site('mom')
      
      barnd_index = 0
      for brand in brands:
        print(brand)
        barnd_index = barnd_index + 1
        print(barnd_index, brand.name_eng)

        url = 'https://www.masterofmalt.com/api/appsearch/search/?currencyid=27&deliverycountryid=352&tradegroupid=0&ext=.json'
        mom_query_data['query'] = brand.name_eng
        res = await fetch_post(mom_headers, session, url, mom_query_data)
        dataset = json.loads(res)
        
        products = []
        for r in dataset['results']:
          def check_data(product_id):
            for sp in stored_products:
              if 'product_id' in sp and product_id == sp['product_id']:
                return True
          
          if check_data(r['id']['raw']) == True:
            continue

          img_url = r['productimage']['raw']
          if 'http' not in img_url:
            img_url = 'https://www.masterofmalt.com' + img_url.replace('/p-IMAGEPRESET', '')
          
          img_uploaded_url = upload_image(img_url, 'mom')
          print(r['title']['raw'], img_url)

          products.append({
            'site': 'mom',
            'brand_id': str(brand.id),
            'product_id': r['id']['raw'],
            'country': r['country']['raw'],
            'distillery': r['distillery']['raw'],
            'description': r['description']['raw'],
            'bottler': r['country']['raw'],
            'name': r['title']['raw'],
            'img': img_uploaded_url,
            'link': 'https://www.masterofmalt.com/'+r['url']['raw'],
            'price': r['price']['raw']
          })

        await insert_product_data(products)


