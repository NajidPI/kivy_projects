# === Comment out before compiling === #
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# === script start === #
from kivy.core.window import Window

#Window.clearcolor = (1, 1, 1, 1)
#Window.size = (360, 600)

from helpers import username_helper

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog


class DemoApp(MDApp):

    def build(self):

        screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        #self.theme_cls.primary_hue = 'A700'
        #self.theme_cls.theme_style = 'Dark'

        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5,
                                                 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)
        screen.add_widget(button)

        return screen

    def show_data(self, obj):

        if self.username.text == "":
            check_string = 'Please enter username'
        else:
            check_string = self.username.text + ' does not exist'

        close_button = MDFlatButton(text='Close',
                                    on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title="Username Check",
                               text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


if __name__ == '__main__':
    app = DemoApp()
    app.run()
