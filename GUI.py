from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random as rand
import time


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        noc = 100
        self.cols = noc #I am a fool

        for x in range(1,(noc * 4)+1):
            a = "{0:.1g}".format(rand.random())
            b = "{0:.1g}".format(rand.random())
            c = "{0:.1g}".format(rand.random())
            d = "{0:.1g}".format(rand.random())
            self.add_widget(Button(background_normal = "", background_color = (a,b,c,d) ))






class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    AwesomeApp().run()
