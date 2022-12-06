import aiohttp
import asyncio
import time
import json
from services.master_of_malt import main as mom
from services.vitatra import main as vitatra
from services.whiskysite import main as whiskysite
from services.whisky_exchange import main as we
from services.htfw import main as ftfw
from services.dali import main as dali

if __name__ == '__main__':
    start = time.time()

    loop = asyncio.get_event_loop()
    tasks = [
        #asyncio.ensure_future(we.main())
        asyncio.ensure_future(dali.main())
        #Easyncio.ensure_future(mom.main()),
        #asyncio.ensure_future(vitatra.main())
        #asyncio.ensure_future(whiskysite.main()),
        #asyncio.ensure_future(ftfw.main())
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print(f"elapsed time = {end - start}s")
    #loop.close()
