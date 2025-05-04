import kivy
kivy.Config.set('graphics', 'resizable', '0')
kivy.Config.set('graphics', 'width', '720')
kivy.Config.set('graphics', 'height', '1080')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import random

count = [0,0]

def new_co():
    return [random.randrange(1,10),random.randrange(1,10)]

def re():
    global count
    count = new_co()
    lable_one = Label(text=str(count[0]))
    lable_two = Label(text=str(count[1]))
    return [lable_one,lable_two]

def st():
    la = re()
    la_one = la[0]
    la_two = la[1]
    b_l.clear_widgets()
    ds = Label(text="*")
    ds.font_size = 150
    la_one.font_size = 150
    la_two.font_size = 150
    b_l.add_widget(la_one)
    b_l.add_widget(ds)
    b_l.add_widget(la_two)
    
b_l = 0

class MainScreen(Screen):
    def __init__(self, **kwargs):
        global b_l
        super(MainScreen, self).__init__(**kwargs)
        b_l = self.layout = BoxLayout(orientation='horizontal')
        st()
        self.layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(hint_text="Введите текст")
        self.button = Button(text="Проверить")
        self.text_input.font_size = 50
        self.button.font_size = 50
        self.button.bind(on_press=self.answer)
        self.layout.add_widget(b_l)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)

    def answer(self, instance):
        global count
        for index in self.text_input.text:
            if not (str(index) in "1234567890"):
                return
        if int(self.text_input.text) == int(count[0])*int(count[1]):
            st()
            self.text_input.text = ""

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == "__main__":
    MyApp().run()