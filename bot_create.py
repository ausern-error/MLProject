
import json
from os.path import exists
keys = ["bot_name", "bot_size","bot_prey","bot_predator","bot_reproduction_rate","bot_adult_age"]
def create_json(file_name,data):
    if exists(file_name) == False:
        with open(file_name, 'w') as file:
          json.dump(data, file)
        return 
    else:
        print("*--could not create a file, file already exists--*")
        quit()
def create_bot_json():
    return create_json(("bot"+(str(input("bot_number: ")))+"_sett.json"),input_data(keys))
def input_data(keys):
    final_data = {}
    for key in keys:
        final_data[key]=input(str(key)+": ")    
    print("*--Pasting following--*\n", final_data)
    return final_data
file_name = create_bot_json()

