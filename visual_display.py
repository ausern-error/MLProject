# Importing libraries
import json
import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout
from arcade.gui import UIFlatButton
import random

# Loading JSON settings file
with open("./input/settings.json") as settings_json:
    settings_json = json.load(settings_json)

# Window size and title
window_width_json = int(settings_json["window_width"])
window_height_json = int(settings_json["window_height"])
window_title = "Machine Learning Simulation"


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        # Loading Fonts and Textures
        self.font_path, self.texture_path = "./data/fonts/", "./data/texture/"
        backgrounds = ["MenuBackground (1).jpg", "MenuBackground (2).jpg", "MenuBackground (3).jpg", "MenuBackground (5).jpg", "MenuBackground (6).jpg"]
        self.fonts = ["TheLastCall-Regular", "CorelDraw", "space age"]

        for font in self.fonts:
            arcade.load_font(self.font_path+font+".ttf")
            print("Loading fonts: "+font+".ttf")
        background = random.choice(backgrounds)
        self.background_texture = arcade.load_texture(self.texture_path+background)

        # Creating text object for titlew
        self.heading_text = arcade.Text(
            "Simulation of Species", self.window.width / 2-880, self.window.height-70,
            arcade.color.WHITE, font_size=50,
            anchor_x="left",
            anchor_y="bottom",
            font_name="space age")
        self.author_text = arcade.Text(
            "By tabish & aslan", self.window.width-200, self.window.height-900,
            arcade.color.WHITE, font_size=14,
            anchor_x="left",
            anchor_y="top",
            font_name="The Last Call")

        # Creating a style for the buttons
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

        # UI Manager for the buttons
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()

        # Creating a vertical box to allign the buttons
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(space_between=20)

        # Creating the button and adding it to the v_box
        simulation_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="START SIMULATION", width=350, height=43, style=button_style
        )
        settings_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Settings", width=350, height=43, style=button_style
        )
        exit_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Exit", width=350, height=43, style=button_style
        )

        self.v_box.add(simulation_button)
        self.v_box.add(settings_button)
        self.v_box.add(exit_button)

        # Creating Widget to center all buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout(x=30, y=-125)
        ui_anchor_layout.add(child=self.v_box, anchor_x="left", anchor_y="top")
        self.ui_manager.add(ui_anchor_layout)

        # Button click events
        simulation_button.on_click = self.on_click_start
        settings_button.on_click = self.on_click_settings
        exit_button.on_click = self.on_click_quit

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
         window_width_json / 2, window_height_json / 2, window_width_json, window_height_json, self.background_texture)
        self.heading_text.draw()
        self.author_text.draw()
        self.ui_manager.draw()

    def on_click_start(self, event):
        print("Line 49 - Changing View to GameView")
        game_view = GameView()
        game_view.on_draw()
        self.window.show_view(game_view)

    def on_click_settings(self, event):
        print("Line 55 - Changing View to SettingsView")
        settings_view = SettingsView()
        settings_view.on_draw()
        self.window.show_view(settings_view)

    def on_click_quit(self, event):
        print("Quit button pressed")
        arcade.exit()


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.JAPANESE_CARMINE)

    def on_draw(self):

        self.clear()


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.MAHOGANY)

    def on_draw(self):
        self.clear()


def main():  # MAIN FUNCTION
    window = arcade.Window(window_width_json, window_height_json, window_title)  # Creates Window
    menu_view = MenuView()
    window.show_view(menu_view)  # Shows MainMenu
    arcade.run()


if __name__ == "__main__":
    main()
