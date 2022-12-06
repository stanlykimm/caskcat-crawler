import requests
cookies = {
    'PHPSESSID': 'ikecd9ahrqbl9aa5tnjjmhk7u0',
    'ForbizCsrfCookieName': '61320e4166692d18eb231100172c3282',
    '_fbp': 'fb.2.1670211746657.1611192878',
    'LAST_CON_TIME': '1670211746',
    'RFID': '000005000000000',
    'VISITORDATE': '20221205',
    'PAGEID': '00000326',
    'UVID': 'f62bca34bec914af25b2c75aec8b8fb1',
    'VID': '5da50202de677ed0c90f884b486bcf18',
    'ajs_anonymous_id': 'b6ad33fb-2f8e-49a3-916f-57922c0661e8',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=ikecd9ahrqbl9aa5tnjjmhk7u0; ForbizCsrfCookieName=61320e4166692d18eb231100172c3282; _fbp=fb.2.1670211746657.1611192878; LAST_CON_TIME=1670211746; RFID=000005000000000; VISITORDATE=20221205; PAGEID=00000326; UVID=f62bca34bec914af25b2c75aec8b8fb1; VID=5da50202de677ed0c90f884b486bcf18; ajs_anonymous_id=b6ad33fb-2f8e-49a3-916f-57922c0661e8',
    'Origin': 'https://www.daligo.co.kr',
    'Referer': 'https://www.daligo.co.kr/shop/goodsList/002000000000000',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'page': '1',
    'max': '1000',
    'filterCid': '002000000000000',
    'orderBy': 'orderCnt',
    'ForbizCsrfTestName': '61320e4166692d18eb231100172c3282',
}

response = requests.post('https://www.daligo.co.kr/controller/product/getGoodsList', cookies=cookies, headers=headers, data=data)
print(response.text)



