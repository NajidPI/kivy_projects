# === Comment out before compiling === #
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)
Window.size = (300, 500)

# === script start === #
from helpers import username_helper, list_helper, screen_helper, navigation_helper, screen_nav

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
from kivy.uix.screenmanager import Screen, ScreenManager




class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='profile'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_nav)
        return screen


if __name__ == '__main__':
    app = DemoApp()
    app.run()
