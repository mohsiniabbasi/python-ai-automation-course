import asyncio
import time

async def ring(name):
    print(f"Ring ring! {name} is calling!")
    await asyncio.sleep(3)
    print(f"{name} has answered.")

async def main():
    await asyncio.gather(ring("Alice"), ring("Bob"), ring("Charlie"))

start = time.time()
asyncio.run(main())
print("Total time:", time.time() - start)