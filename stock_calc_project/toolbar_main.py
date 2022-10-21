# === Comment out before compiling === #
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)
Window.size = (300, 500)

# === script start === #
from helpers import username_helper, list_helper, screen_helper

from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
from kivy.lang import Builder
# from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.list import MDList, ThreeLineIconListItem
# from kivymd.uix.list import IconRightWidget, ImageLeftWidget, ImageRightWidget, ThreeLineAvatarListItem
# from kivy.uix.scrollview import ScrollView
# from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    app = DemoApp()
    app.run()
