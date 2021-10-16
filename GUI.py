from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp

class Battle_Roll_All_GUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.attack_result = StringProperty("You rolled to hit.")





        for player in range(4):
            cell = Battle_cell(size_hint = (1, 1))
            self.add_widget(cell)


class Battle_cell(BoxLayout):
    pass

class BRAApp(App):
    pass


BRAApp().run()