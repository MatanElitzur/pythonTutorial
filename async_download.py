import asyncio
import aiohttp
from urllib import request

# This code example how multi threding is better in perormence then single threding.

def download():
    return request.urlopen('https://google.com').read()

def synchronus():
    for _ in range(5):
        download()
    
async def asynchronus():
    async with aiohttp.ClientSession() as session:
        coroutines = [async_download(session, 'https://google.com') for _ in range(5)]
        await asyncio.gather(*coroutines) # The * is for unpacks the list of coroutines, The gather function waits for all the coroutines to finish

async def async_download(session, url):
    async with session.get(url) as response:
        return await response.text()

@profile
def main():
    synchronus()
    asyncio.run(asynchronus())
# Execute --> kernprof -l -v async_download.py    
