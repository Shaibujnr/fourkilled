from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty,StringProperty,ObjectProperty,ListProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Four_Killed(Widget):
    pass
class Four_KilledApp(App):
    def build(self):
        return Four_Killed()
    
if __name__=='__main__':
    Four_KilledApp().run()
