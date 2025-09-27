import time
import random

wallet = 0

print("⛏️ Starting mining simulation...")

for i in range(10):
    mined = round(random.uniform(0.0001, 0.01), 6)
    wallet += mined
    print(f"Block {i+1}: +{mined} BTC")
    time.sleep(1)

print("Mining finished. Total mined:", wallet, "BTC")
