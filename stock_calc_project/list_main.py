# === Comment out before compiling === #
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# === script start === #
from kivy.core.window import Window

#Window.clearcolor = (1, 1, 1, 1)
#Window.size = (360, 600)

from helpers import username_helper, list_helper

from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
from kivy.lang import Builder
#from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
#from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, ThreeLineIconListItem
from kivymd.uix.list import IconRightWidget, ImageLeftWidget, ImageRightWidget, ThreeLineAvatarListItem
#from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem


class DemoApp(MDApp):

    def build(self):

        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range(20):

            image = ImageLeftWidget(source="coin.png")
            items = ThreeLineAvatarListItem(text='Item ' + str(i),
                                            secondary_text="Hello World",
                                            tertiary_text="Third Text")
            items.add_widget(image)
            self.root.ids.container.add_widget(items)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
