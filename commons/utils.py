import json

async def fetch_post(headers, session, url, data):
    async with session.post(url, data=json.dumps(data),
                            headers=headers) as response:
        return await response.text()

async def fetch_get(headers, session, url):
    async with session.get(url, headers=headers) as response:
        return await response.text()

async def fetch_get_proxy(headers, session, url, proxy):
    async with session.get(url, headers=headers, proxy=proxy) as response:
        return await response.text()

def get_proxy_list():
    lists = [
        '20.214.223.91:3128', '101.79.15.198:80', '52.231.137.170:3128', '59.15.28.113:3128', 
        '20.249.40.3:3128', '20.214.64.219:3128', '20.214.219.129:3128', '121.190.16.109:3128', 
        '3.34.13.110:80', '101.79.242.72:8080', '220.82.71.96:3128']
    return lists


    