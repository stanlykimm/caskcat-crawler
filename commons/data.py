mom_headers = {
    "Origin": "https://www.masterofmalt.com",
    "Host": "www.masterofmalt.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Referer": "https://www.masterofmalt.com/distilleries/the-macallan-whisky-distillery/?q=Macallan&size=n_25_n",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}
mom_query_data = {
    'query': '',
    'facets': {
        'isbestseller': {
            'type': 'value',
        },
        'stocklevel': {
            'type': 'value',
        },
        'price': {
            'type': 'range',
            'ranges': [
                {
                    'from': 0,
                    'to': 2147483647,
                    'name': 'Show all',
                },
                {
                    'from': 0.01,
                    'to': 50,
                    'name': '₩0.00 – ₩79,698.31',
                },
                {
                    'from': 50,
                    'to': 100,
                    'name': '₩79,698.31 – ₩159,396.61',
                },
                {
                    'from': 100,
                    'to': 200,
                    'name': '₩159,396.61 – ₩318,793.23',
                },
                {
                    'from': 200,
                    'to': 400,
                    'name': '₩318,793.23 – ₩637,586.45',
                },
                {
                    'from': 400,
                    'to': 2147483647,
                    'name': '₩637,586.45 +',
                },
            ],
        },
        'userrating': {
            'type': 'range',
            'ranges': [
                {
                    'from': 0,
                    'name': 'Show all',
                },
                {
                    'from': 5,
                    'name': '5 ⭐ only',
                },
                {
                    'from': 4,
                    'name': '4 ⭐ and up',
                },
                {
                    'from': 3,
                    'name': '3 ⭐ and up',
                },
                {
                    'from': 2,
                    'name': '2 ⭐ and up',
                },
                {
                    'from': 1,
                    'name': '1 ⭐ and up',
                },
            ],
        },
        'volume': {
            'type': 'range',
            'ranges': [
                {
                    'from': 35,
                    'to': 36,
                    'name': '35',
                },
                {
                    'from': 50,
                    'to': 51,
                    'name': '50',
                },
                {
                    'from': 70,
                    'to': 71,
                    'name': '70',
                },
                {
                    'from': 75,
                    'to': 76,
                    'name': '75',
                },
                {
                    'from': 100,
                    'to': 101,
                    'name': '100',
                },
            ],
        },
        'targettemplate': {
            'type': 'value',
        },
        'style': {
            'type': 'value',
        },
        'country': {
            'type': 'value',
        },
        'distillery': {
            'type': 'value',
            'size': 100,
        },
        'region': {
            'type': 'value',
        },
        'isdiscounted': {
            'type': 'value',
        },
        'hasdram': {
            'type': 'value',
        },
        'age': {
            'type': 'range',
            'ranges': [
                {
                    'from': 0,
                    'to': 100,
                    'name': '0 - 100',
                },
            ],
        },
        'vintage': {
            'type': 'range',
            'ranges': [
                {
                    'from': 1850,
                    'to': 2022,
                    'name': '1850 - 2022',
                },
            ],
        },
        'bottlingyear': {
            'type': 'range',
            'ranges': [
                {
                    'from': 1850,
                    'to': 2022,
                    'name': '1850 - 2022',
                },
            ],
        },
        'abv': {
            'type': 'range',
            'ranges': [
                {
                    'from': 0,
                    'to': 100,
                    'name': '0 - 100',
                },
            ],
        },
    },
    'result_fields': {
        'country': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'urltitle': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'releasedate': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'comingsoon': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'isdiscontinued': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'score': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'price': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'fullproduct': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'distilleryurl': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'volume': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'atomstock': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'stockincoming': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'rrp': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'hasactivelightningdeal': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'vintage': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'style': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'bottlingyear': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'region': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'preorder': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'previousprice': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'distillery': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'hasdram': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'description': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'bottler': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'title': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'stocklevel': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'productimage': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'isdiscounted': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'productstatus': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'discountflag': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'hasfreeshipping': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'userrating': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'maxnumberpercustomer': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'searchfield': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'url': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'hasfreeshippingworldwide': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'targettemplate': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'reviewcount': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'abv': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'ranking': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'isvatableproduct': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'age': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'id': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'freestock': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
        'isbestseller': {
            'raw': {},
            'snippet': {
                'size': 100,
                'fallback': True,
            },
        },
    },
    'page': {
        'size': 25,
        'current': 1,
    },
}

vitatra_headers = {
    "Origin": "https://www.vitatra.de",
    "Host": "www.vitatra.de",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Referer": "https://www.vitatra.de/product/category/689-690/page/0?orderby=%EC%9D%B8%EA%B8%B0%EC%88%9C",
    "Connection": "keep-alive"
}

whiskysite_headers = {
    "Origin": "https://www.whiskysite.nl",
    "Host": "www.whiskysite.nl",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Referer": "https://www.whiskysite.nl/",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

we_headers = {
    "Origin": "https://www.thewhiskyexchange.com",
    "Host": "www.thewhiskyexchange.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Referer": "hhttps://www.thewhiskyexchange.com",
    "Connection": "keep-alive",
}

htfw_headers = {
    "Origin": "https://www.htfw.com",
    "Host": "www.htfw.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Referer": "https://www.htfw.com",
    "Connection": "keep-alive"
}

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; Samsung Chromebook Plus (V2) Build/R107-15117.112.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/100 Mobile/15E148 Version/15.0',
    'Mozilla/5.0 (Linux; Android 10; Aquaris X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.1.0; RCT6A03W13E Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Safari/537.36',
    'Mozilla/5.0 (Android 9; Mobile; rv:106.0) Gecko/106.0 Firefox/106.0'
]

dailyshot_headers = {
    "Origin": "https://dailyshot.co",
    "Host": "dailyshot.co",
    "User-Agent": "",
    "Referer": "https://dailyshot.co/pickup/products/4/detail/",
    "Connection": "keep-alive"
}

dali_headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    "Origin": "https://www.daligo.co.kr",
    "Host": "www.daligo.co.kr",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Referer": "https://www.daligo.co.kr/shop/goodsList/",
    "Connection": "keep-alive"
}

tyndrum_headers = {
    "Origin": "https://www.tyndrumwhisky.com",
    "Host": "www.tyndrumwhisky.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Referer": "https://www.tyndrumwhisky.com/blends-grains/blended-malts.html",    
}

def get_ds_header():
    import random
    random.shuffle(user_agents)
    referer_url = 'https://dailyshot.co/pickup/products/%s/detail/' % (random.randint(1, 1000))
    dailyshot_headers['User-Agent'] = user_agents[0]
    dailyshot_headers['Referer'] = referer_url
    return dailyshot_headers