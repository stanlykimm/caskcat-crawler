headers = {
    "Origin": "https://www.masterofmalt.com",
    "Host": "www.masterofmalt.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Referer": "https://www.masterofmalt.com/distilleries/the-macallan-whisky-distillery/?q=Macallan&size=n_25_n",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}
query_data = {
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