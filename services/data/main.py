import re
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.product import get_all_products, update_prouct

async def main():
    async with aiohttp.ClientSession() as session:
      for product in await get_all_products():
        #print(product)
        rg1, rg2 = re.compile('([0-9]+)(\,?[0-9]+)?%'), re.compile('([0-9]+)(\.?[0-9]+)?%')
        rs1, rs2 = rg1.findall(product['name']), rg2.findall(product['name'])
        
        rg_year1 = re.compile('([0-9]+)? [Yy]ear+s? [Oo]ld')
        rg_year2 = re.compile('([0-9]+)?[Yy][Oo]?')
        rs_year1 = rg_year1.findall(product['name'])
        rs_year2 = rg_year2.findall(product['name'])
        #print(rs_year2)
        year = ''
        if rs_year1 == [] and rs_year2 == []:
          year = 'NAS'
        elif rs_year1 != []:
          year = rs_year1[0]
        elif rs_year2 != []:
          year = rs_year2[0]
        else:
          pass
        
        abv = ''
        if rs1 == [] and rs2 == []:
          continue
        else:
          if rs1[0][1] != '':
            abv = ''.join(map(str, rs1[0]))
          elif rs1[0][1] == '' and rs2[0][1] == '':
            abv = rs1[0][0]
          elif rs2[0][1] != '':
            abv = ''.join(map(str, rs2[0]))
        if abv == '100':
          abv = ''

        update_row = {'year': year, 'abv': abv}
        await update_prouct(product['_id'], update_row)
        print(product['name'])
        print(update_row)
        print(rs_year1, rs_year2)
        

          

