import aiohttp
import asyncio
import time
import json
from services.dali import backblaze as bb

if __name__ == '__main__':
    start = time.time()

    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(bb.main())
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print(f"elapsed time = {end - start}s")
    #loop.close()
