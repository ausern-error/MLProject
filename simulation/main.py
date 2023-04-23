import time
import entity_structures
import clock
last_tick_time = time.time()
tick_speed = 60
clock = clock.Clock(180)
while True:
    sleep = 1 / tick_speed - (time.time() - last_tick_time)
    last_tick_time = time.time()
    if sleep > 0:
        time.sleep(sleep)
        clock.tick()
        print(clock.day_counter)
