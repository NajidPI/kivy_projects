# === Comment out before compiling === #
#from kivy import Config
#Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)
#Window.size = (300, 500)

# === script start === #
# from helpers import *

import sqlite3

from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
# from kivymd.uix.list import MDList, ThreeLineIconListItem
# from kivymd.uix.list import IconRightWidget, ImageLeftWidget, ImageRightWidget, ThreeLineAvatarListItem
# from kivy.uix.scrollview import ScrollView
# from kivymd.uix.list import OneLineListItem
# from kivymd.uix.datatables import MDDataTable
# from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Stocks:
    
    def __init__(self, quantity, buy, profit = 0, sell = 0):
        
        self.quantity = quantity
        self.buy = buy
        
        purchase_value = quantity*buy
        if purchase_value < 5000:
            self.FEE = 14.95
        elif purchase_value < 20000:
            self.FEE = 19.95
        else:
            self.FEE = 25.02
        
        self.dp = len(str(buy).split('.')[1])
        self.profit = profit
        
        if sell == 0:
            self.sell = self.buy
        else:
            self.sell = sell

    # Rounding function
    def roundTraditional(val,digits):
        return round(val+10**(-len(str(val))-1), digits)
    
    # Find selling price per unit
    def Sell(self):
        value = Stocks.roundTraditional((self.buy*self.quantity)+self.FEE,2)
        break_even = value+(self.FEE*2)
        surplus_sell = break_even+self.profit
        true_sell = surplus_sell/self.quantity
        result = Stocks.roundTraditional(true_sell,self.dp)
        return Stocks.roundTraditional(surplus_sell,self.dp), result
    
    def Profit(self):
        value = Stocks.roundTraditional((self.buy*self.quantity)+self.FEE,2)
        break_even = value+(self.FEE*2)
        value =  Stocks.roundTraditional((self.quantity*self.sell)+self.FEE,2)
        result = Stocks.roundTraditional(value - break_even, self.dp)
        return result

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CalculatorScreen(Screen):
    pass


class WelcomeScreen(Screen):
    pass


class Quote(Screen):
    pass

sm = ScreenManager()
sm.add_widget(CalculatorScreen(name='calculator'))
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(Quote(name='quote'))



class DemoApp(MDApp):

    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_file('helpers.kv')
        return screen

    def show_data(self, number, price, profit, selling):

        error_string = 'Try again :('


        if number == '' or price == '':
            self.result = error_string

        if profit == '':
            profit = 0

        if selling == '':
            selling = 0

        try:
            number = int(number)
            price = float(price)
            profit = float(profit)
            selling = float(selling)

            if selling == 0:
                values = Stocks(number,price,profit,selling).Sell()
                self.result = f"{values[0]} Mkt. value"
                self.result = self.result+ '\n' + f"{values[1]} Mkt. price"
            elif profit == 0:
                self.result = f"{Stocks(number,price,profit,selling).Profit()} Total Profit"

        except:
            self.result = error_string

        close_button = MDFlatButton(text='Close',
                                    on_release=self.close_dialog)
        self.dialog = MDDialog(title="Result",
                               text=self.result,
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()




    def get_random_quote(self):
        rs = (None, None)
        try:
            conn = sqlite3.connect('db/randomquotes.db')
            c = conn.cursor()
            c.execute( 'SELECT quote, author FROM quotes ORDER BY RANDOM() LIMIT 1')
            rs = c.fetchone()   
        except sqlite3.Error:
            pass
        finally:
            conn.close()
    
        data = {'quote': rs[0], 'author': rs[1]}
        
        return data
    
    def display_quote(self):
        random_quote = self.get_random_quote()
        result = r'"%s"%s-- %s' % \
            (random_quote['quote'], '\n' * 2, random_quote['author'])
        close_button = MDFlatButton(text='Close',
                                    on_release=self.close_dialog)
        self.dialog = MDDialog(title="Quote",
                               text=result,
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()




if __name__ == '__main__':
    app = DemoApp()
    app.run()
