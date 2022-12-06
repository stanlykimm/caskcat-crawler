import aiohttp
import asyncio
import time
import json
from services.dailyshot import main as ds

if __name__ == '__main__':
    start = time.time()

    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(ds.main())
        #Easyncio.ensure_future(mom.main()),
        #asyncio.ensure_future(vitatra.main())
        #asyncio.ensure_future(whiskysite.main()),
        #asyncio.ensure_future(ftfw.main())
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print(f"elapsed time = {end - start}s")
    #loop.close()
