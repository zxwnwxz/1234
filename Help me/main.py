from kivy.config import Config
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import json
Window.size = (350, 500)

def Click():
    print('Click is working')
    

class MyApp(App):
    def build(self):
        txt = Label(text='Text')
        btn1 = Button(text='1')
        btn2 = Button(text='2')
        btn3 = Button(text='3')
        btn4 = Button(text='+')
        btn5 = Button(text='4')
        btn6 = Button(text='5')
        btn7 = Button(text='6')
        btn8 = Button(text='-')
        btn9 = Button(text='7')
        btn10 = Button(text='8')
        btn11 = Button(text='9')
        btn12 = Button(text='.')
        btn13 = Button(text='0')
        btn14 = Button(text='*')
        btn15 = Button(text='/')
        btn16 = Button(text='=')
        btn17 = Button(text='DEL')
        btn18 = Button(text='Test button')
        btn18.on_press = Click

        main = BoxLayout(orientation='vertical')

        layout_text = BoxLayout()                    
        layout = BoxLayout(orientation='horizontal')
        layout1 = BoxLayout(orientation='horizontal')
        layout2 = BoxLayout(orientation='horizontal')
        layout3 = BoxLayout(orientation='horizontal')
        layout4 = BoxLayout(orientation='horizontal')

        layout_text.add_widget(txt)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        layout1.add_widget(btn5)
        layout1.add_widget(btn6)
        layout1.add_widget(btn7)
        layout1.add_widget(btn8)
        layout2.add_widget(btn9)
        layout2.add_widget(btn10)
        layout2.add_widget(btn11)
        layout2.add_widget(btn12)
        layout3.add_widget(btn13)
        layout3.add_widget(btn14)
        layout3.add_widget(btn15)
        layout3.add_widget(btn16)
        layout4.add_widget(btn17)
        layout4.add_widget(btn18)


        main.add_widget(layout_text)
        main.add_widget(layout)
        main.add_widget(layout1)
        main.add_widget(layout2)
        main.add_widget(layout3)
        main.add_widget(layout4)
        return main

MyApp().run()