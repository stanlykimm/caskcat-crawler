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


json_data = {
  "operationName":"getProduct",
  "variables":{
    "currentPage":1,
    "categoryId": "",
    "pageSize":20,
    "filters":{},
    "sort":{
      "price":"ASC"
    },
    "search":"bowmore"
  },
  "query":"query getProduct($pageSize: Int!, $currentPage: Int!, $filters: ProductAttributeFilterInput!, $sort: ProductAttributeSortInput!, $search: String) {  products(filter: $filters, pageSize: $pageSize, currentPage: $currentPage, sort: $sort, search: $search) {    total_count    page_info {      page_size      total_pages      current_page      __typename    }    sort_fields {      options {        label        value        __typename      }      default      __typename    }    aggregations {      attribute_code      count      label      options {        count        label        value        __typename      }      __typename    }    items {      id      name      cask_number      badge      region      sku      created_at      manufacturer      url_key      custom_attributes {        code        value        __typename      }      new_from_date      image {        url        __typename      }      small_image {        url        __typename      }      price {        regularPrice {          amount {            value            currency            __typename          }          __typename        }        __typename      }      __typename    }    __typename  }}"
}

async def main():
    async with aiohttp.ClientSession() as session:
      brands = await get_brands()
      stored_products = await get_products_by_site('twb')

      brand_index = 0
      for brand in brands:
        brand_index = brand_index + 1
        print(brand_index, brand.name_eng)

        json_data['search'] = brand.name_eng

        url = 'https://www.thewhiskybarrel.com/graphql'
        res = await fetch_post(twb_headers, session, url, json_data)
        dataset = json.loads(res)

        products = []
        for prd in dataset['data']['products']['items']:
          def check_data(product_id):
            for sp in stored_products:
              if 'product_id' in sp and product_id == sp['product_id']:
                return True
          
          if check_data(prd['id']) == True:
            continue

          products.append({
            'site': 'wtb',
            'product_id': prd['id'],
            'name': prd['name'],
            'img': upload_image(prd['image']['url'], 'twb'),
            'link': 'https://www.thewhiskybarrel.com/' + prd['url_key'],
            'price': prd['price']['regularPrice']['amount']['value'],
          })
        if len(products) == 0:
          print('products is empty')
        else:
          await insert_product_data(products)    