from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os, random
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.core.window import Window

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):






if __name__ == '__main__':
    app = MainApp()
    app.run()
