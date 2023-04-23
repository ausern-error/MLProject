
class Clock:

    def __init__(self,day_length:int):
        self.day_length = day_length
        self.tick_counter: int = 0
        self.day_counter: int = 0
    def tick(self):
        self.tick_counter += 1
        if self.tick_counter % self.day_length == 0:
            self.day_counter+=1
