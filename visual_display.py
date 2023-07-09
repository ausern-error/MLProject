#  Importing Libraries
import json
import random
import arcade
import simulation
import os
from arcade.gui import *


# Loading JSON settings file
with open("./input/settings.json") as settings_json:
    settings_json = json.load(settings_json)

# Importing Settings From JSON
WINDOW_WIDTH = int(settings_json["window_width"])
WINDOW_HEIGHT = int(settings_json["window_height"])
WINDOW_TITLE = str(settings_json["window_title"])

# Sprite Settings
SPRITE_SCALE = int(1)

arcade.enable_timings()  # Enables Timing For FPS & STATS

class MenuView(arcade.View):  # MENU VIEW
    def __init__(self):
        super().__init__()

        self.font_path = "./data/fonts/"  # Texture Path
        self.texture_path = "./data/texture/MenuBackgrounds/"  # texture path
        
        backgrounds = ["MenuBackground (1).jpg", "MenuBackground (2).jpg",
                    "MenuBackground (3).jpg", "MenuBackground (4).jpg"]  # Texture File Names
        self.fonts = ["TheLastCall-Regular", "CorelDraw", "space age"]  # Font File Names

        # Loads Fonts
        for font in self.fonts:
            arcade.load_font(self.font_path + font + ".ttf")
            print("Succesfully Loaded Font: : " + font + ".ttf")

        # Loads Background Texture
        background = random.choice(backgrounds)
        self.background_texture = arcade.load_texture(self.texture_path + background)

        # Creating text object for heading & author
        self.heading_text = arcade.Text(
            "Simulation of Species", self.window.width-1890, self.window.height-75,
            arcade.color.WHITE, font_size=50,
            anchor_x="left",
            anchor_y="bottom",
            font_name="space age")
        self.author_text = arcade.Text(
            "By tabish & aslan", self.window.width-200, self.window.height-1030,
            arcade.color.WHITE, font_size=14,
            anchor_x="left",
            anchor_y="top",
            font_name="The Last Call")

        # Button Style
        button_style = {
            "normal": UIFlatButton.UIStyle(
                font_size=15,
                font_name="CorelDraw",
                font_color=arcade.color.NAVAJO_WHITE,
                bg=arcade.color.TRANSPARENT_BLACK,
                border=None,
                border_width=2
            ),
            "hover": UIFlatButton.UIStyle(
                font_size=15,
                font_name="CorelDraw",
                font_color=arcade.color.BLACK,
                bg=arcade.color.ANTIQUE_WHITE,
                border=arcade.color.EERIE_BLACK,
                border_width=3
            ),
            "press": UIFlatButton.UIStyle(
                font_size=15,
                font_name="CorelDraw",
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
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(space_between=15, align="right")  # Vertical Box

        # Creates Buttons
        simulation_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Start Simulation", width=350, height=43, style=button_style)
        settings_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Settings", width=350, height=43, style=button_style)
        exit_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Exit", width=350, height=43, style=button_style)

        # Adds Buttons To The Vertical Box
        self.v_box.add(simulation_button)
        self.v_box.add(settings_button)
        self.v_box.add(exit_button)

        # Creates Widget
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout(x=30, y=-110)
        ui_anchor_layout.add(child=self.v_box, anchor_x="left", anchor_y="top")
        self.ui_manager.add(ui_anchor_layout)

        # Button Click Events
        simulation_button.on_click = self.on_click_StartSimulation
        settings_button.on_click = self.on_click_settings
        exit_button.on_click = self.on_click_quit

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
            self.window.width / 2, self.window.height / 2, self.window.width, self.window.height, self.background_texture) #  Draws Wallpaper
        self.heading_text.draw()  # Draws Heading Text
        self.author_text.draw()  # Draws Author Text
        self.ui_manager.draw()  # Draws Buttons

    # Button Functions
    def on_click_StartSimulation(self, event):
        print("View Change To GameView")
        self.ui_manager.disable()  # Unloads buttons
        game_view = GameView()
        self.window.show_view(game_view)  # Changes View


    def on_click_settings(self, event):
        print("View Change To SettingsView")
        self.ui_manager.disable()  # Unloads buttons
        settings_view = SettingsView()
        settings_view.on_draw()
        self.window.show_view(settings_view)  # Changes View


    def on_click_quit(self, event):
        print("Quit button pressed")
        arcade.close_window()  # Quits Arcade

class GameView(arcade.View):  # GAME VIEW
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
        
        # Performance
        self.fps_text = None
        self.self.arcade_texture_list = dict()
        self.sprite_texture_path = "./data/texture/SpriteTexture/"  # Path To Sprite Texture

        with open(os.path.join(self.sprite_texture_path,"texture_list.json")) as texture_json:
            texture_list = json.load(texture_json)
        
        for texture in texture_list:
            self.arcade_texture_list[texture] = arcade.load_texture(os.path.join(self.sprite_texture_path,texture_list[texture][texture_name]),0,0,texture_list[texture][width],texture_list[texture][height])
        self.entity_manager = simulation.entity_structures.EntityManager(list())
        a = simulation.entity_structures.Animal(entity_structures.Vector2(0,0),"animal_sheep",entity_manager,"test",3,15,10,1,2,3,list(),list(),entity_structures.Task.wander,{"food":resources.AnimalResourceRequirements(True,True,3,(0,10),(0,10))} )

    def setup(self):

        # Performance
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

        #TODO: OPTIMISE THIS
        for entity in self.entity_manager.entities:
            temp_texture = self.arcade_texture_list[entity.texture_name]
            arcade.draw_texture_rectangle(entity.position.x,entity.position.y,temp_texture.width,temp_texture.height,temp_texture)
        
        # Performance
        self.fps_text = arcade.Text(  # Updates FPS
        text=f"FPS:{round(arcade.get_fps())}",
        start_x=10, start_y=1049,
        color=arcade.color.ALMOND)
        
        arcade.print_timings()  # Prints Activity
        self.fps_text.draw()  # Draws FPS

    def on_update(self, delta_time):
        for entity in self.entity_manager.entities:
            entity.update()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.MenuView_Change()

    def MenuView_Change(self):
        print("View Change To MenuView")
        menu_view = MenuView()
        menu_view.on_draw()
        self.window.show_view(menu_view)


class SettingsView(arcade.View):  # SETTINGS VIEW
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.JAPANESE_CARMINE)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.MenuView_Change()

    def MenuView_Change(self):
        print("View Change To MenuView")
        menu_view = MenuView()
        menu_view.on_draw()
        self.window.show_view(menu_view)

    def on_draw(self):
        self.clear()


def main():  # MAIN FUNCTION
    window = arcade.Window(  # Creates window
        width=WINDOW_HEIGHT,
        height=WINDOW_WIDTH,
        title=WINDOW_TITLE,
        antialiasing=True,
        enable_polling=True,
        fullscreen=True
        )
    
    menu_view = MenuView()
    window.show_view(menu_view)  # Changes View To Menu
    arcade.run()


if __name__ == "__main__":
    main()
