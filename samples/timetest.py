import time

start = time.time()
time.sleep(3)

# You must convert to milliseconds:
dt = int((time.time() - start) * 1000)

print dt
