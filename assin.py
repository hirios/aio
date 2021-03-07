
import asyncio
import aiohttp



async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def req():
    print('one')
    async with aiohttp.ClientSession() as session:
        async with session.get('https://raw.githubusercontent.com/hirios/zenitsu/master/permition') as html:
            print(await html.text())

    print('two')

    
async def main():
    await asyncio.gather(req(), req(), req())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
