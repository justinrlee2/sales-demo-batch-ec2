import time
import requests

print("Starting python script...")
print("Getting sector performance...")
r = requests.get('https://financialmodelingprep.com/api/sectors-performance')
print(r.text)
print("Processing code (sleep for 30 seconds)...")

time.sleep(6)
print("20%")

time.sleep(6)
print("40%")

time.sleep(6)
print("20%")

time.sleep(6)
print("80%")

time.sleep(6)
print("100%")

print("Done!")
