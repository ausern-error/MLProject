from datetime import datetime
import os
import json
class Stats:
    def __init__(self):
        self.populations = dict()
    def create_json(self):
        with open(os.path.join(".","output",datetime.now().strftime("%d%m%Y%H%M%S")+".json"), "w") as file:
            json.dump(self.populations, file)