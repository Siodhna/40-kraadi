# File name: 40kraadi.py
from __future__ import print_function, division
import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
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
from kivy.properties import ObjectProperty
from random import randint

Window.clearcolor = get_color_from_hex('#000000')

class EsimeneLehekulg(Screen):
    pass

class Mang(Screen):
    uus_tegevus = StringProperty()
    popup1 = Popup()
    popup2 = Popup()
    def __init__(self,**kwargs):
        super(Mang,self).__init__(**kwargs)
        f = open('tegevused.txt', 'r')
        k = list(f)
        self.uus_tegevus = str(k[randint(0,len(k)-1)])




    def Muuda_Tegevust(self):
        f = open('tegevused.txt', 'r')
        k = list(f)
        self.uus_tegevus = str(k[randint(0,len(k)-1)])

    def popupvalja1(self):
        popup1 = Popup1()
        popup1.open()

    def popupvalja2(self):
        popup2 = Popup2()
        popup2.open()




class Popup1(Popup):
    pass


class Popup2(Popup):
    pass





class Abi(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("40kraadi.kv")

class NelikummendKraadiApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    NelikummendKraadiApp().run()