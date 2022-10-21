# === Comment out before compiling === #
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# === script start === #
from kivy.core.window import Window

# Window.clearcolor = (1, 1, 1, 1)
# Window.size = (360, 600)

from helpers import username_helper, list_helper

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivy.lang import Builder
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

        screen = Screen()
        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            rows_num=10,
                            column_data=[
                            ("No.", dp(18)),
                            ("Food", dp(20)),
                            ("Calories", dp(20))
                            ],
                            row_data=[
                            ("1", "Burger", "300"),
                            ("2", "Oats", "150"),
                            ("3", "Oats", "150"),
                            ("4", "Oats", "150"),
                            ("5", "Oats", "150"),
                            ("6", "Oats", "150"),
                            ("7", "Oats", "150"),
                            ("8", "Oats", "150"),
                            ("9", "Oats", "150")
                            ]
                            )
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)

        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
