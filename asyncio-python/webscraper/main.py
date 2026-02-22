import asyncio
import aiohttp
import time


async def fetch(url: str, session: aiohttp.ClientSession) -> dict:
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with session.get(url, timeout=timeout) as response:
            content = await response.text()
            await asyncio.sleep(2)
            return {
                "url": url,
                "status": response.status,
                "content_length": len(content),
            }
    except asyncio.TimeoutError:
        return {"url": url, "error": "Timeout"}
    except aiohttp.ClientError as e:
        return {"url": url, "error": str(e)}


async def concurrent():
    urls = [
        "https://dummyjson.com/products",
        "https://dummyjson.com/users",
        "https://dummyjson.com/posts",
    ]

    start = time.time()

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(url, session) for url in urls])
    end = time.time() - start
    print(f"Fetched {len(results)} URLs in {end:.2f}s")
    for result in results:
        print(result)


async def one_by_one():
    urls = [
        "https://dummyjson.com/products",
        "https://dummyjson.com/users",
        "https://dummyjson.com/posts",
    ]
    results = []
    start = time.time()

    async with aiohttp.ClientSession() as session:
        for url in urls:
            result = await fetch(url, session)
            # print(result)
            results.append(result)
    end = time.time() - start
    print(f"Fetched {len(results)} URLs in {end:.2f}s")
    for result in results:
        print(result)


async def rate_limited():
    urls = [
        "https://dummyjson.com/products",
        "https://dummyjson.com/users",
        "https://dummyjson.com/posts",
        "https://dummyjson.com/carts",
        "https://dummyjson.com/recipes",
        "https://dummyjson.com/quotes",
    ]
    semaprone = asyncio.Semaphore(6)
    start = time.time()

    async def fetch_with_limit(url):
        async with semaprone:
            return await fetch(url, session)

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_with_limit(url) for url in urls])
    end = time.time() - start
    print(f"Fetched {len(results)} URLs in {end:.2f}s")
    for result in results:
        print(result)


asyncio.run(one_by_one())
asyncio.run(concurrent())
asyncio.run(rate_limited())
