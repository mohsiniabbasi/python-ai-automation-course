import time

def ring(name):
    print(f"Ring ring! {name} is calling!")
    time.sleep(3)
    print(f"{name} has answered.")

start = time.time()
ring("Alice")
ring("Bob")
ring("Charlie")
print("Total time:", time.time() - start)