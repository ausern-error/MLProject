# Importing libraries
import arcade
import json
import arcade.gui

# Loading JSON settings file
with open("./input/settings.json") as settings_json:
    settings_json = json.load(settings_json)

window_width_json = int(settings_json["window_width"])
window_height_json = int(settings_json["window_height"])
window_title = "Machine Learning Simulation"


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.load_font("./data/fonts/Freedom-10eM.ttf")  # loading custom fonts from a dir
        arcade.load_font("./data/fonts/Konimasa-yO9m.ttf")
        arcade.load_font("./data/fonts/ToThePointRegular-n9y4.ttf")
        arcade.set_background_color(arcade.color.BITTERSWEET)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=5)  # vertical box to allign buttons
        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Simulation", width=200)
        self.v_box.add(start_button)

        settings_button = arcade.gui.UIFlatButton(
            text="Settings",
            width=200)
        self.v_box.add(settings_button)

        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        start_button.on_click = self.on_click_start
        settings_button.on_click = self.on_click_settings

    def on_click_start(self, event):
        print("Line 49 - Changing View Window to GameView")
        game_view = GameView()
        game_view.on_draw()
        self.window.show_view(game_view)

    def on_click_settings(self, event):
        print("Line 55 - Changing View Window to SettingsView")
        settings_view = SettingsView()
        settings_view.on_draw()
        self.window.show_view(settings_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()
        arcade.draw_text("ML SIMULATION", self.window.width / 2, self.window.height / 2+180, arcade.color.WHITE,
                         font_size=70, anchor_x="center", font_name="FREEDOM")
        arcade.draw_text("Aslan & Muhktar", 20, 15, arcade.color.WHITE, font_size=20,
                         anchor_y="bottom", font_name="KONIMASA", bold=True)


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("Line 15 - Quit class used")
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
