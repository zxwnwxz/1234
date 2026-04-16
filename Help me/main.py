from kivy.config import Config
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import json


Window.size = (350, 500)


class MyApp(App):
    def build(self):
        self.text = Label(text='0', font_size=40, size_hint=(1, 1))
        self.current_input = ''
        self.result_shown = False


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
        btn18 = Button(text='CLR')
 

        btn1.on_press = self.press_1
        btn2.on_press = self.press_2
        btn3.on_press = self.press_3
        btn4.on_press = self.press_plus
        btn5.on_press = self.press_4
        btn6.on_press = self.press_5
        btn7.on_press = self.press_6
        btn8.on_press = self.press_minus
        btn9.on_press = self.press_7
        btn10.on_press = self.press_8
        btn11.on_press = self.press_9
        btn12.on_press = self.press_tochka
        btn13.on_press = self.press_0
        btn14.on_press = self.press_ymozhenie
        btn15.on_press = self.press_delenie
        btn16.on_press = self.calculate
        btn17.on_press = self.delete_last
        btn18.on_press = self.delete_all



        main = BoxLayout(orientation='vertical')

        layout_text = BoxLayout()                    
        layout = BoxLayout(orientation='horizontal')
        layout1 = BoxLayout(orientation='horizontal')
        layout2 = BoxLayout(orientation='horizontal')
        layout3 = BoxLayout(orientation='horizontal')
        layout4 = BoxLayout(orientation='horizontal')

        layout_text.add_widget(self.text)
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

    
    def update_font_size(self):
        text_lenght = len(self.text.text)

        if text_lenght <= 8:
            new_size = 40
        elif text_lenght <= 10:
            new_size = 35
        elif text_lenght <= 12:
            new_size = 30
        elif text_lenght <= 14:
            new_size = 25
        elif text_lenght <= 16:
            new_size = 20
        elif text_lenght <= 18:
            new_size = 18
        elif text_lenght <= 20:
            new_size = 16
        else:
            new_size = 14
        self.text.font_size = new_size


    def press_1(self):
        self.add_number('1')
    
    def press_2(self):
        self.add_number('2')

    def press_3(self):
        self.add_number('3')

    def press_4(self):
        self.add_number('4')

    def press_5(self):
        self.add_number('5')

    def press_6(self):
        self.add_number('6')

    def press_7(self):
        self.add_number('7')

    def press_8(self):
        self.add_number('8')

    def press_9(self):
        self.add_number('9')

    def press_0(self):
        self.add_number('0')

    def press_tochka(self):
        self.add_number('.')

    

    def press_plus(self):
        self.add_operator('+')

    def press_minus(self):
        self.add_operator('-')
    
    def press_ymozhenie(self):
        self.add_operator('*')
    
    def press_delenie(self):
        self.add_operator('/')





    def add_number(self, num):
        if self.result_shown:
            self.current_input = ''
            self.result_shown = False
        self.current_input += num
        if self.current_input:
            self.text.text = self.current_input
        else:
            self.text.text = '0'
        self.update_font_size()

    def add_operator(self, op):
        if self.current_input and self.current_input[-1] not in '+-*/':
            self.current_input += op
            self.text.text = self.current_input
            self.result_shown = False
            self.update_font_size()

    def delete_last(self):
        self.current_input = self.current_input[:-1]
        if self.current_input:
            self.text.text = self.current_input
        else:
            self.text.text = '0'
        self.result_shown = False
        self.update_font_size()

    def delete_all(self):
        self.current_input = ''
        self.text.text = '0'
        self.result_shown = False
        self.update_font_size()

    def calculate(self):
        try:
            if not self.current_input:
                return
            if '/0' in self.current_input:
                self.text.text = 'Error'
                self.current_input = ''
                self.result_shown = True
                return
            
            result = eval(self.current_input)
            if isinstance(result, float):
                result = round(result, 10)
                if result == int(result):
                    result = int(result)
            
            self.text.text = str(result)
            self.current_input = str(result)
            self.result_shown = True 
            self.update_font_size()
        except:
            self.text.text = 'Error'
            self.current_input = ''
            self.result_shown = True

MyApp().run()