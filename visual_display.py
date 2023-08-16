#  Importing Libraries
import json
import random
import arcade
import random
from simulation import entity_structures,resources,clock,event_manager, output
import matplotlib.pyplot as plt

import time

import os
from arcade.gui import *

#set up randomness
random.seed()

# Loading JSON settings file
with open("./data/settings.json") as settings_json:
    settings_json = json.load(settings_json)

# Importing Settings From JSON
WINDOW_WIDTH = int(settings_json["window_width"])
WINDOW_HEIGHT = int(settings_json["window_height"])
WINDOW_TITLE = str(settings_json["window_title"])

MAP_WIDTH = int(settings_json["map_width"])
MAP_HEIGHT = int(settings_json["map_height"])




# Sprite Settings
SPRITE_SCALE = int(1)

#Font names
fonts = ["Ticketing", "novem___", "arcadeclassic", "lunchds"]

arcade.enable_timings()  # Enables Timing For FPS & STATS

def font_loader(fonts):
    font_path = "./data/fonts/"
    for font in fonts:
        arcade.load_font(font_path + font + ".ttf")
        print("Succesfully Loaded Font: : " + font + ".ttf")

class Cloud(arcade.Sprite):
    def __init__(self, texture, scale):
        super().__init__(texture, scale=scale)

        # Velocity
        self.change_x = random.uniform(0.4, 1.5)
        self.change_y = 0

        self.position = (
            random.randrange(0, 1400),
            random.randrange(WINDOW_HEIGHT-400, WINDOW_HEIGHT-270)
        )

    def update(self):
        self.position = (
            self.position[0] + self.change_x,
            self.position[1] + self.change_y

        )
        
        # Velocity
        self.change_x = random.uniform(0.4, 1.5)
        self.change_y = 0
        
        if self.position[0] > 1980:
            self.center_x = 0
            self.center_y = random.randrange(650, 860)


class MenuView(arcade.View):  # MENU VIEW
    def __init__(self):
        super().__init__()
        self.stats = output.Stats()

        self.texture_path = "./data/texture/MenuBackgrounds/"  # texture path

        backgrounds = ["menu_background (1).png"]  # Texture File Names 

        # Loads Background Texture
        background = random.choice(backgrounds)
        self.background_texture = arcade.load_texture(
            self.texture_path + background)

        # Creating text object for heading & author
        self.heading_text = arcade.Text(
            "Evolving  Simulations  of  Animal  Behavior", self.window.width/2, self.window.height/2+100     ,
            arcade.color.WHITE, font_size=50,
            anchor_x="center",
            anchor_y="bottom",
            font_name="Ticketing")
        self.author_text = arcade.Text(
            "By Tabish & Aslan", self.window.width-250, self.window.height-1030,
            arcade.color.WHITE, font_size=18,
            anchor_x="left",
            anchor_y="top",
            font_name="November")

        # Button Style
        button_style = {
            "normal": UIFlatButton.UIStyle(
                font_size=16,
                font_name="lunchtime doubly so",
                font_color=arcade.color.NAVAJO_WHITE,
                bg=arcade.color.TRANSPARENT_BLACK,
                border=None,
                border_width=2
            ),
            "hover": UIFlatButton.UIStyle(
                font_size=18,
                font_name="lunchtime doubly so",
                font_color=arcade.color.BLACK,
                bg=arcade.color.ANTIQUE_WHITE,
                border=arcade.color.EERIE_BLACK,
                border_width=3
            ),
            "press": UIFlatButton.UIStyle(
                font_size=18,
                font_name="lunchtime doubly so",
                font_color=arcade.color.WARM_BLACK,
                bg=arcade.color.LIGHT_GRAY,
                border=arcade.color.DAVY_GREY,
                border_width=3
            )
        }

        # UI Manager For Buttons
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()

        # Creates Vertical Box
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(
            space_between=15, align="center")  # Vertical Box

        # Creates Buttons
        simulation_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Start Simulation", width=350, height=43, style=button_style)
        exit_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Exit", width=350, height=43, style=button_style)

        # Adds Buttons To The Vertical Box
        self.v_box.add(simulation_button)
        self.v_box.add(exit_button)

        # Creates Widget
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout(
            x=30, y=-110)
        ui_anchor_layout.add(child=self.v_box)
        self.ui_manager.add(ui_anchor_layout)

        # Button Click Events
        simulation_button.on_click = self.on_click_StartSimulation
        exit_button.on_click = self.on_click_quit

        #cute cloudies
        self.cloud_list = None
        self.cloud_textures = [self.texture_path+"cloud_texture (1).png", self.texture_path+"cloud_texture (2).png", self.texture_path+"cloud_texture (3).png"]
        self.arr_len = len(self.cloud_textures)
    
    def add_clouds(self, amount):  # TODO: Reference Window for Spawning of Clouds
        for i in range(amount):
            cloud = Cloud(self.cloud_textures[(random.randrange(0, self.arr_len))], random.uniform(0.8, 1.7))
            self.cloud_list.append(cloud)

    def setup(self):
        self.cloud_list = arcade.SpriteList(use_spatial_hash=False)
        self.add_clouds(9)

        arcade.schedule(self.update, 1/60)
    
    def update(self, delta_time):
        self.cloud_list.update()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
            self.window.width / 2, self.window.height / 2, self.window.width, self.window.height, self.background_texture)  # Draws Wallpaper
        self.cloud_list.draw()
        self.heading_text.draw()  # Draws Heading Text
        self.author_text.draw()  # Draws Author Text
        self.ui_manager.draw()  # Draws Buttons

        


    # Button Functions
    def on_click_StartSimulation(self, event):
        print("View Change To SimulationView")
        self.ui_manager.disable()  # Unloads buttons
        simulation_view = SimulationView(self.stats)          
        self.window.show_view(simulation_view)  # Changes View

    def on_click_quit(self, event):
        print("Quit button pressed")
        arcade.close_window()  # Quits Arcade



class SimulationView(arcade.View):      
    def __init__(self,stats):
        super().__init__()
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
        #camera
        self.camera = arcade.Camera(viewport=(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
        self.fps_text = None
        self.arcade_texture_list = dict()
        self.path_to_data = os.path.join(".","data")
        self.sprite_texture_path = "./data/texture/SpriteTexture/"  # Path To Sprite Texture
        self.stats = stats
        with open(os.path.join(self.sprite_texture_path, "texture_list.json")) as texture_json:
            texture_list = json.load(texture_json)

        for texture in texture_list:
            self.arcade_texture_list[texture] = arcade.load_texture(os.path.join(
                self.sprite_texture_path, texture_list[texture]["texture_name"]))
            #self.arcade_texture_list[texture].width = texture_list[texture]["width"]
            #self.arcade_texture_list[texture].height = texture_list[texture]["height"]

            self.arcade_texture_list[texture].size = (texture_list[texture]["width"],texture_list[texture]["height"])
        self.clock = clock.Clock(5)
        self.entity_manager = entity_structures.EntityManager(list(),entity_structures.Vector2(MAP_WIDTH,MAP_HEIGHT),self.clock,stats)
        
        self.resource_manager = resources.ResourceManager(self.path_to_data)
        for path in os.listdir(os.path.join(self.path_to_data, "animals")):
            with open(os.path.join(self.path_to_data, "animals",path)) as animal:
                decoded_animal = json.load(animal)
                stats.populations[decoded_animal["animal_type"]] = 0
                stats.populations_per_day[decoded_animal["animal_type"]] = list()
                entity_structures.Animal.load(decoded_animal,self.entity_manager)
        self.simulation_background = entity_structures.Entity(entity_structures.Vector2(0,0),self.entity_manager,"simulation_background")
        #event manager
        self.event_manager = event_manager.EventManager(self.entity_manager,self.resource_manager,self.clock,MAP_WIDTH,MAP_HEIGHT)


    def setup(self):
        self.fps_text = arcade.Text(
            text=f"FPS:{round(arcade.get_fps())}",
            start_x=10, start_y=1049,
            color=arcade.color.ALMOND
        )

    def on_show_view(self):
        self.setup()

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.camera.use()
        #TODO: OPTIMISE THIS
        for entity in self.entity_manager.entities:
            if entity.texture_name in self.arcade_texture_list:
                temp_texture = self.arcade_texture_list[entity.texture_name]
                temp_texture.draw_scaled(entity.position.x,entity.position.y,1)
                #temp_texture.draw_sized(entity.position.x,entity.position.y,temp_texture.width,temp_texture.height)
                #arcade.draw_texture_rectangle(entity.position.x,entity.position.y,temp_texture.width,temp_texture.height,temp_texture)
            if type(entity) is entity_structures.Animal:
                #arcade.Text( text=str(entity.hunt_per_day),start_x=entity.position.x, start_y=entity.position.y,color=arcade.color.BLACK,font_size=16).draw()    
                pass

        text = "" 
        for animal_name,animal_population in self.stats.populations.items():
            text +=str(animal_name)+":"+str(animal_population)
        arcade.Text(text=text,start_x=WINDOW_WIDTH-150,start_y=WINDOW_HEIGHT-30,color=arcade.color.RED).draw()
        arcade.Text(  # Updates FPS
            text=f"FPS:{round(arcade.get_fps())}",
            start_x=0, start_y=0,
            color=arcade.color.ALMOND).draw()
        arcade.Text(  # current day
            text="day:" + str(self.clock.day_counter),
            start_x=WINDOW_WIDTH-150, start_y=WINDOW_HEIGHT-20,
            color=arcade.color.ALMOND).draw()
    def on_update(self, delta_time):
        for entity in self.entity_manager.entities:
            entity.update(delta_time)

        self.clock.tick(delta_time)
        if self.clock.new_day:
            for key, value in self.entity_manager.stats.populations.items():
                self.entity_manager.stats.populations_per_day[key].append(value)
        self.event_manager.update(delta_time)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.MenuView_Change()

    def MenuView_Change(self):
        print("View Change To MenuView")
        menu_view = MenuView()
        menu_view.setup()
        self.window.show_view(menu_view)


def main():  # MAIN FUNCTION
    window = arcade.Window(  # Creates window
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        title=WINDOW_TITLE,
        antialiasing=True,
        enable_polling=True,
        fullscreen=True
        #TODO: test on different refresh rates
        )
    
    
    font_loader(fonts)
    menu_view = MenuView()
    menu_view.setup()
    window.show_view(menu_view)  # Changes View To Menu
    arcade.run()
    menu_view.stats.create_json()
    figure, plots = plt.subplots(2, 1)
    plots[0].bar(menu_view.stats.populations.keys(),menu_view.stats.populations.values())
    plots[0].set_title("Final Populations")
    plots[0].set_ylabel("Population")
    plots[0].set_xlabel("Animal")
    for key, value in menu_view.stats.populations.items():
        menu_view.stats.populations_per_day[key].append(value)
    for key,value in menu_view.stats.populations_per_day.items():
        plots[1].plot(value,label=str(key))
    plots[1].set_title("Final Population Per Day")
    plots[1].set_ylabel("Population")
    plots[1].set_xlabel("Days")
    plt.legend(loc='upper center')
    plt.show()

if __name__ == "__main__":
    main()

