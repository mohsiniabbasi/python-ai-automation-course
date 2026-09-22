from dotenv import load_dotenv
import os
load_dotenv()

name = os.getenv("DRIVER_NAME")
print("Driver: ", name)

key = os.getenv("TEST_API_KEY")
print("Key found: ", key)