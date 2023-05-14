import time
import entity_structures
import clock
last_tick_time = time.time()
tick_speed = 60
clock = clock.Clock(180)
entity_manager = entity_structures.EntityManager(list())
a = entity_structures.Entity(entity_structures.Vector2(0,0),"test",3,15,10,1,2,3,list(),list(),entity_structures.Task.wander,entity_manager)
print(a.task)

while True:
    sleep = 1 / tick_speed - (time.time() - last_tick_time)
    last_tick_time = time.time()
    if sleep > 0:
        time.sleep(sleep)
        clock.tick()
        for entity in entity_manager.entities:
            entity.update()

