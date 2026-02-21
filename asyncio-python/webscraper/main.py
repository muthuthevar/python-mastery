import asyncio
import aiohttp


async def main():
    print("Hello world")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dummyjson.com/products") as products:
            print(await products.json())
            print(products.status)
            print(await products.text())


if __name__ == "__main__":
    asyncio.run(main())
