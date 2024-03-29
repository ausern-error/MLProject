class Clock:
    def __init__(self,day_length:int): #day_length in secconds
        self.day_length = day_length
        self.timer: int = 0
        self.day_counter: int = 0
        self.new_day = True
    def tick(self,delta_time):
        if self.timer > 0:
            self.timer -= delta_time
            self.new_day = False
        else:
            self.day_counter+=1
            self.timer = self.day_length
            self.new_day = True