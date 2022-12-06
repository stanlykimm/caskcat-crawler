import time
import logging
import random
import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
from commons.utils import *
from commons.brand import *
from commons.data import *
from repositories.brand import get_brand_by_name
from repositories.dailyshot import get_row, insert_product_data

logging.basicConfig(level=logging.INFO)

async def main():
    async with aiohttp.ClientSession() as session:
      product_ids = list(range(1,3004))
      random.shuffle(product_ids)

      del_products = [
          2515, 131, 2810, 1950, 2543, 2665, 2779, 2097, 2511, 871, 1821, 2561, 
          2859, 2750, 1623, 2633, 107, 2951, 1369, 1975, 2736, 1822, 1771, 1883, 
          646, 1563, 2235, 2680, 132, 1507, 2839, 2508, 2818, 2744, 858, 2142, 
          2435, 1963, 2808, 2141, 128, 2690, 2209, 2289, 2330, 2924, 879, 
          2771, 2995, 1102, 2997, 1948, 1948, 2054, 882, 2851, 2098, 391, 2108, 
          802, 642, 206, 2019, 2794, 2210, 2070, 2928, 2527, 2208, 2716, 1450, 
          2630, 2969, 2069, 2752, 1893, 68, 2936, 2507, 2316, 1788, 2699, 2285, 
          2073, 2641, 2950, 2743, 376, 2510, 2603, 1576, 2962, 2544, 1367, 
          628, 2684, 84, 2803, 2594, 75, 2993, 2575, 1781, 130, 2388, 2964, 
          2909, 134, 2872, 498, 2503, 2831, 2979, 867, 2785, 2978, 2381, 
          1892, 2442, 2466, 2704, 2385, 2867, 1559, 2246, 2436, 641, 566, 1591, 
          2067, 1951, 567, 2281, 2502, 2563, 629, 2694, 494, 2287, 2361, 631, 
          2567, 2568, 1964, 2753, 2953, 415, 129, 1462, 249, 2832, 983, 
          2830, 2842, 2841, 2099, 2734, 2790, 2980, 2783, 219, 2715, 1811, 
          2938, 2970, 2672, 137, 2922, 2772, 463, 2965, 1768, 2653, 2500, 2109, 878, 207, 2238, 
          2068, 2492, 2232, 2919, 2866, 2236, 2878, 147, 2306, 96, 2445, 2930, 2574, 1985, 205, 
          1558, 2319, 2324, 2182, 2857, 2711, 2096, 886, 686, 1789, 2177, 881, 83, 2314, 2615, 
          2331, 2910, 2532, 2409, 1873, 2566, 1820, 649, 2920, 2222, 1986, 448, 2101, 2152, 2767, 
          2408, 2072, 2948, 2971, 2888, 2777, 2364, 2291, 74, 2206, 1425, 2775, 462, 2730, 2504, 2691, 
          2957, 2829, 2640, 1072, 2858, 2290, 636, 2283, 1955, 2113, 326, 2556, 2880, 2935, 644, 2318, 
          2081, 1770, 1865, 2860, 2769, 2651, 2400, 2737, 1350, 2538, 1485, 2074, 2781, 1983, 2439, 2131, 
          2960, 2169, 2104, 2681, 2244, 2130, 2846, 2382, 2949, 2931, 2804, 2628, 2733, 2913, 1727, 2865, 
          138, 2956, 643, 2387, 2813, 2542, 2642, 2977, 1773, 640, 2461, 2855, 648, 2118, 1905, 2093, 369, 
          535, 1990, 2664, 710, 2434, 2968, 1108, 2618, 2071, 536, 2027, 2229, 2963, 2312, 623, 2341, 2411, 
          2307, 2579, 1769, 2645, 2854, 2332, 2410, 2483, 2075, 2547, 1766, 2784, 78, 869, 2102, 2178, 1657, 
          223, 2746, 1067, 806, 1608, 2333, 2754, 647, 2713,
          2873, 2861, 2856, 866, 2925, 687, 534, 2966, 1508, 2100, 2106, 2129, 777, 1071, 1070, 1471, 375, 2282, 2742, 106, 1710, 1996, 2780, 2745, 2514, 957, 2692, 1639, 2472, 2882, 2573, 828, 2315, 2768, 2447, 2487, 2412, 2834, 136, 135, 2809, 2321, 2144, 2438, 2501, 2482, 2095, 2393, 1953, 2700, 2657, 2505, 2491, 1894, 2056, 1989, 2776, 1069, 2847, 2812, 2778, 926, 2490, 2025, 254, 1982, 2686, 880, 917, 2107, 2565, 986, 1949, 2835, 2383, 632, 2624, 2079, 2696, 2078, 2509, 2583, 2334, 2954, 1189, 633, 2747, 2972, 387, 1860, 626, 2151, 639, 127, 2806, 2446, 2927, 2153, 2921, 2828, 95, 2219, 2305, 133, 872, 606, 2124, 2294, 2912, 2741, 2481, 2485, 2569, 2682, 2774, 2875, 2546, 1987, 1776, 2836, 2250, 2342, 650, 2929, 2619, 2237, 2558, 2679, 2413, 102, 2240, 2077, 2868, 2536, 410, 2143, 1929, 1765, 2939, 2877, 2770, 230, 1786, 1952, 2386, 1699, 82, 2499, 2871, 2751, 2899, 241, 1944, 2392, 2773, 2174, 2286, 2571, 2735, 2040, 2837, 140, 2365, 86, 2384, 2441, 2076, 2506, 1907, 2811, 622, 2976, 252, 1674, 2066, 2576, 2814, 2146, 2230, 2675, 2712, 1486, 2186, 1921, 1979, 101, 630, 2683, 2996, 2967, 1844, 2293, 2349, 2621, 2623, 2732, 2132, 2355, 2564, 2608, 2622, 1837, 2932, 862, 2787, 67, 2923, 247, 103, 2673, 2145, 1726, 2802, 2788, 2572, 2852, 2134, 2869, 1197, 2876, 1606, 2874, 2934, 1784, 2870, 2363, 2833, 2562, 2749, 2607, 2317, 98, 2223, 2389, 2786, 956, 706, 1988, 2308, 1800, 2688, 2050, 2821, 1911, 2952, 2918, 2631, 1954, 1913, 2685, 1998, 2933, 2228, 1767, 2552, 2838, 1638, 2671, 2748, 2437, 356, 2545, 2632, 2907, 2414, 2926, 1997, 2548, 2042, 1655, 2220, 2020, 2705, 2710, 1792, 2853, 2577, 1774, 2702, 374, 2973, 2433, 2695, 683, 1936, 1132, 2701, 143, 2105, 2697, 2049, 2961, 2864, 2147, 2720
      ]
      proxy_servers = get_proxy_list()
      product_ids = list(set(product_ids) - set(del_products))

      empty_product = []
      random.shuffle(product_ids)
      for number in product_ids:
        random.shuffle(proxy_servers)

        row = await get_row(number)

        if row is None:
          try:
            logging.info('proxy server : %s' % (proxy_servers[0]))
            proxy_server = 'http://%s' % (proxy_servers[0])

            url = 'https://dailyshot.co/pickup/products/%s/detail/' % (number)
            logging.info('request url : %s' % url)
            res = await fetch_get(get_ds_header(), session, url)
            soup = BeautifulSoup(res, "lxml")

            product = {}
            product['product_id'] = number
            try:
              product['name_en'] = soup.find('p', {'class':'en-name'}).text.strip()
            except:
              product['name_en'] = ''

            try:
              product['name_kr'] = soup.find('p', {'class':'ko-name'}).text.strip()
            except:
              logging.info('찾을수 없는 상품')
              empty_product.append(number)
              logging.info(empty_product)
              continue

            try:
              product['image'] = soup.find('img', {'id':'thumbnail-image'})['src']
            except:
              lddata = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))
              product['image'] = lddata['itemReviewed']['image'][0]

            try:
              product['price'] = soup.find('div', {'class':'market-avg-price'}).find('del').text.strip()
              price_el = soup.find('div', {'class':'price-sub-container'}).find_all('span')
              product['price_percent'] = price_el[0].text.strip()
              product['price_discount'] = price_el[1].text.strip()
            except:
              product['price'] = 0
              product['price_percent'] = 0
              product['price_discount'] = 0


            def get_info(row):
              return  {
                'label': row.select_one('.label').text.strip(),
                'content': row.select_one('.content').text.strip()
              }

            note = []
            for row in soup.find_all('div', {'class': 'tasting-note-row'}):
              note.append(get_info(row))
            
            info = []
            for row in soup.find_all('div', {'class': 'product-info-row'}):
              info.append(get_info(row))
            
            product['note'] = note
            product['info'] = info

            logging.info(product)
            await insert_product_data(product)
            
          except Exception:
            import traceback
            traceback.print_exc()
        else:
          continue
        rf = random.uniform(2, 5)
        time.sleep(rf)
        print('-----%s-----' % (rf))
        print('------------------------------------------------')
        