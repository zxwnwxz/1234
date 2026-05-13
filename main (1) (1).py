from kivy.config import Config
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.utils import get_color_from_hex
import json
import os

#импорты сверху, снизу размер окна

Window.size = (350, 500)    

# создание класса билд, для постановки приложений, изменений цвета, расположение
class MyApp(App):
    def build(self):
        
        self.title = 'Calculator'
        self.icon = 'calculator_icon.png'

        Window.clear_color = get_color_from_hex('#0F172A')
        self.text = Label(
            text='0',

            halign='center',
            valign='middle'
        )
        self.text.bind(size=self._update_text_size)
        
        self.current_input = ''
        self.result_shown = False
#           создание кнопачек
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
        btn19 = Button(text='Full History')

                # обводка кнопачек и цвета
        all_buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, 
                       btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19]
        
        for btn in all_buttons:
            btn.background_normal = ''  
            btn.background_color = (0, 0, 0, 0)  
            btn.color = get_color_from_hex('#F8FAFC') 
            
            with btn.canvas.before:
                Color(rgba=get_color_from_hex("#000000B5"))
                btn.bg_shape = RoundedRectangle(pos=btn.pos, size=btn.size, radius=[5])
                
                Color(rgba=get_color_from_hex('#64748B'))
                btn.bg_line = Line(
                    rounded_rectangle=(btn.x, btn.y, btn.width, btn.height, 10, 10, 10, 10), 
                    width=1.2
                )
            
            def update_btn_graphics(obj, val):
                obj.bg_shape.pos = obj.pos
                obj.bg_shape.size = obj.size
                obj.bg_line.rounded_rectangle = (obj.x, obj.y, obj.width, obj.height, 10, 10, 10, 10)

            btn.bind(pos=update_btn_graphics, size=update_btn_graphics)

#               Добавление функции к кнопкам, чтобы они создавали действие

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
        btn19.on_press = self.open_history

# Лейауты, там где стоят кнопачки

        main = BoxLayout(orientation='vertical', spacing=10, padding=10)
        with main.canvas.before:
            self.bg_rect = Rectangle(source='background.jpg', pos=main.pos, size=main.size)
        main.bind(pos=lambda obj, val: setattr(self.bg_rect, 'pos', val),
                  size=lambda obj, val: setattr(self.bg_rect, 'size', val))

        layout_text = BoxLayout()                    
        layout = BoxLayout(orientation='horizontal', spacing=10)
        layout1 = BoxLayout(orientation='horizontal', spacing=10)
        layout2 = BoxLayout(orientation='horizontal', spacing=10)
        layout3 = BoxLayout(orientation='horizontal', spacing=10)
        layout4 = BoxLayout(orientation='horizontal', spacing=10)

# Добавление кнопок на лейауты

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
        layout4.add_widget(btn19)

#лейауты и текст для нижней панели калькулятора

        main.add_widget(layout_text)
        main.add_widget(layout)
        main.add_widget(layout1)
        main.add_widget(layout2)
        main.add_widget(layout3)
        main.add_widget(layout4)
        # self.history_label = Label(text='History:\n', font_size=14, size_hint=(1, 1))
        self.history_box = BoxLayout(orientation='vertical')
        main.add_widget(self.history_box)



        self.update_history()
        return main

#создание появлений дествии, в данном случае появление истории
    
    def update_history(self):
        self.history_box.clear_widgets()

        if not os.path.exists('text.txt'):
            self.history_box.add_widget(
                Label(
                    text='(пусто)',
                    font_size=14,
                    halign='left',
                    valign='middle'
                )
            )
            return

        with open('text.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        last_lines = lines[-5:]

        title = Label(text='------------:ИСТОРИЯ:-----------', font_size=13.5, halign='center')
        title.bind(size=title.setter('text_size'))
        self.history_box.add_widget(title)

        for line in reversed(last_lines):
            lbl = Label(
                text=line.strip(),
                font_size=14,
                halign='left',
                valign='middle'
            )
            lbl.bind(size=lbl.setter('text_size'))
            self.history_box.add_widget(lbl)

#кнопки, и их начало работы

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

    def open_history(self):
        os.startfile("text.txt")


# Появление чисел на экране

    def add_number(self, num):
        if self.result_shown:
            self.current_input = ''
            self.result_shown = False

        self.current_input += num

        if self.current_input:
            self.update_display(self.current_input)
        else:
            self.update_display('0')

#оператор который может создавать действия +-*/

    def add_operator(self, op):
        if self.current_input and self.current_input[-1] not in '+-*/':
            self.current_input += op
            self.update_display(self.current_input)
            self.result_shown = False

#Удаление последних симболов

    def delete_last(self):
        self.current_input = self.current_input[:-1]

        if self.current_input:
            self.update_display(self.current_input)
        else:
            self.update_display('0')

        self.result_shown = False

#Удаление всего текста

    def delete_all(self):
        self.current_input = ''
        self.update_display('0')
        self.result_shown = False

#Сохранение текста в файл

    def save_to_file(self, expression, result):
        if expression.isdigit() or expression.replace('.', '', 1).isdigit():
            return

        if not any(op in expression for op in '+-*/'):
            return

        if str(expression) == str(result):
            return

        with open('text.txt', 'a', encoding='utf-8') as f:
            line = expression + '=' + str(result) + '\n'
            f.write(line)

#отоброжение цифор на экране

    def update_display(self, new_text):
        self.text.text = new_text

        self.text.font_size = 50
        self.text.texture_update()

        max_width = self.text.width - 20

        while self.text.texture_size[0] > max_width and self.text.font_size > 20:
            self.text.font_size -= 1
            self.text.texture_update()

        self.text.halign = 'center'
        self.text.valign = 'middle'
        self.text.text_size = self.text.size

#обновление размера текста, чтобы при переход на новую строчку он не был маленьким

    def _update_text_size(self, instance, value):
        instance.text_size = instance.size

#ДЕЙСТВИЕ КАЛЬКУЛЯТОР! Сам мозг проекта, который все умножает и складывает, и если число невозможно, то не ломается, а пишет ошибку

    def calculate(self):
        try:
            if not self.current_input:
                return

            result = eval(self.current_input)

            if result == float('inf') or result == float('-inf'):
                raise ZeroDivisionError

            if isinstance(result, float):
                result = round(result, 10)
                if result == int(result):
                    result = int(result)

            self.save_to_file(self.current_input, result)
            self.update_history()

            self.update_display(str(result))
            self.current_input = str(result)
            self.result_shown = True

        except ZeroDivisionError:
            self.update_display('Error')
            self.current_input = ''
            self.result_shown = True

        except:
            self.update_display('Error')
            self.current_input = ''
            self.result_shown = True

#Запуск приложения!

MyApp().run()