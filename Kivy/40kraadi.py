# File name: 40kraadi.py
import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.animation import AnimationTransition
from kivy.uix.textinput import TextInput
from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color
from kivy.graphics import Canvas
import random
from kivy.properties import ObjectProperty
from random import randint

Window.clearcolor = get_color_from_hex('#51555b')
class EsimeneLehekulg(Screen):
    pass


class MangijateValik(Screen):
    pass

class Mang(Screen):
    uus_tegevus = StringProperty()
    def __init__(self,**kwargs):
        super(Mang,self).__init__(**kwargs)
        f = open('tegevused.txt', 'r')
        k = list(f)
        self.uus_tegevus = str(k[randint(0,len(k)-1)])
    def Muuda_Tegevust(self):
        f = open('tegevused.txt', 'r')
        k = list(f)


        self.uus_tegevus = str(k[randint(0,len(k)-1)])
class Blank(Screen):
    pass


class ManguKaart(Label):
    pass

class KraadiMang(Widget):
    kaart = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player3 = ObjectProperty(None)

class Abi(Screen):
    pass
class Seaded(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("40kraadi.kv")

class NelikummendKraadiApp(App):


    def build(self):





        return presentation




if __name__ == "__main__":
    NelikummendKraadiApp().run()