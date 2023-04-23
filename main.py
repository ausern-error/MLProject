import time
import entity_structures
last_tick_time = time.time()
tick_speed = 60
while True:
    sleep = 1 / tick_speed - (time.time() - last_tick_time)
    last_tick_time = time.time()
    if sleep > 0:
        time.sleep(sleep)
 
