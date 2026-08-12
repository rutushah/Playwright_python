import asyncio
import time


def task(name):
    print(f"Starting task : {name}")
    time.sleep(2)
    print(f"Finishing task : {name}")
    
# task("Learning python")
# task("Learning java")


# for async

async def task(name):
    print(f"Starting task : {name}")
    await asyncio.sleep(2)
    print(f"Finishing task : {name}")

async def main():
    await asyncio.gather(
        task("Learning python"),
        task("Learning java")
    )

asyncio.run(main())