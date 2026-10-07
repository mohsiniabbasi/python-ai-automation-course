import asyncio

async def ring(name):
    print(f"Ring ring! {name} is calling!")
    await asyncio.sleep(3)
    print(f"{name} has answered.")

asyncio.run(ring("Alice"))