import kivy
kivy.require("1.8.0")
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from random import randint
from kivy.core.text import LabelBase
Window.clearcolor = get_color_from_hex('#000000')


class EsimeneLehekulg(Screen):
    pass


class Mang(Screen):
    uus_tegevus = StringProperty()
    popup1 = Popup()
    popup2 = Popup()
    uus_pilt = StringProperty()

    def __init__(self, **kwargs):
        super(Mang, self).__init__(**kwargs)
        f = open('tegevused.txt', 'r')
        k = list(f)
        listike = list(open('tahed.txt'))
        self.uus_pilt = str(listike[randint(0, len(listike)-1)])
        self.uus_tegevus = str('[b]' + k[randint(0, len(k)-1)] + '[/b]')

    def muuda_tegevust(self, *args):
        k = list(open('tegevused.txt'))
        listike = list(open('tahed.txt'))
        self.uus_tegevus = str('[b]' + k[randint(0, len(k)-1)] + '[/b]')
        self.uus_pilt = str(listike[randint(0, len(listike)-1)])

    def popupvalja1(self):
        popup1 = Popup1()
        popup1.open()

    def popupvalja2(self):
        popup2 = Popup2()
        popup2.open()


class Popup1(Popup):
    onnitlus = StringProperty()

    def __init__(self, **kwargs):
        super(Popup1, self).__init__(**kwargs)
        fail = open('onnitlused.txt')
        onnitlused = list(fail)
        self.onnitlus = str('[b]' + onnitlused[randint(0, len(onnitlused) - 1)] + ' \n  Anna telefon edasi![/b]')


class Popup2(Popup):
    kaebus = StringProperty()

    def __init__(self, **kwargs):
        super(Popup2, self).__init__(**kwargs)
        fail = open('kaebused.txt')
        kaebused = list(fail)
        self.kaebus = str('[b]'+kaebused[randint(0, len(kaebused)-1)]+'\n  Anna telefon edasi![/b]')


class Abi(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")


class NelikummendKraadiApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    LabelBase.register(name='Modern Pictograms',
                       fn_regular='modernpics.ttf')
    LabelBase.register(name='capture',
                       fn_regular='Capture_it.ttf')
    LabelBase.register(name='evil',
                       fn_regular='EVILZ.ttf')
    LabelBase.register(name='santiago',
                       fn_regular='SANTIAGO_ICONO.ttf')
    NelikummendKraadiApp().run()
