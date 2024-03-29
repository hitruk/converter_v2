
# 1. Switch frame
# 2. Создать два фрейма WinFirst, WinSecond которые будут переключаться в виджете LabelFrame
# 3. Настроить переключение WinFirst, WinSecond в классе View
# 4. MVC модель

import tkinter as tk
from tkinter.constants import *
from tkinter import ttk


class Model():
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self_value
    
    @value.setter
    def value(self, x):
        if type(x) in [int, float]:
            self._value = x
        else:
            raise TypeError(f'In class Model: invalid data type: {type(x)}')
    # https://www.mile-to-km.com/km-to-miles.php
    def mi_to_km(self):
        km = self._value * 1.609344
        return km
    
    def km_to_mi(self):
        mi = self._value / 1.609344
        return mi

class WinFirst(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=1, pady=2, fill=BOTH, expand=True)

        # contant
        self.label = ttk.Label(self, text='Km to miles')  # Win First
        self.label.pack()

        options = {'padx':2, 'pady':2, 'anchor':W}

        # ENTRY
        self.type_entry = tk.StringVar(value=0)
        self.entry = ttk.Entry(self, textvariable= self.type_entry)
        self.entry.pack(**options)
        
        # BUTTON
        self.button = ttk.Button(self, text='Click', command=self.click_button)
        self.button.pack(**options)

        # RESULT
        self.res_label = ttk.Label(self, text='RESULT:')
        self.res_label.pack()

        # FULL RESULT
        self.full_result = ttk.Label(self, text='0.0 km = 0.0 mi')
        self.full_result.pack()

        # set controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def click_button(self):
        if self.controller:
            try:
                entry_value = float(self.type_entry.get())
                self.controller.convert(entry_value)
            except ValueError as error:
                print(f'In class WinFirst: {error}')

    def set_full_result(self, x, text):
        self.full_result['text'] = f'{x} km = {text} mi' 

class WinSecond(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=1, pady=2, fill=BOTH, expand=True)

        # contant
        self.label = ttk.Label(self, text='Miles to km')  # Win Second
        self.label.pack()

        options = {'padx':2, 'pady':2, 'anchor':W}

        # ENTRY
        self.type_entry = tk.StringVar(value=0)
        self.entry = ttk.Entry(self, textvariable= self.type_entry)
        self.entry.pack(**options)
        
        #BUTTON
        self.button = ttk.Button(self, text='Click', command=self.click_button)
        self.button.pack(**options)

        #RESULT
        self.res_label = ttk.Label(self, text='RESULT:')
        self.res_label.pack()

        # FULL RESULT
        self.full_result = ttk.Label(self, text='0.0 mi = 0.0 km')
        self.full_result.pack()

        # set controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def click_button(self):
        if self.controller:
            try:
                entry_value = float(self.type_entry.get())
                self.controller.convert(entry_value)
            except ValueError as error:
                print(f'In class WinFirst: {error}')

    def set_full_result(self, x, text):
        self.full_result['text'] = f'{x} km = {text} mi' 

class SetFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self['text'] = 'Settings'
        self.pack(padx=1, pady=2, fill=BOTH, expand=True)

        # contant
        options = {'padx':2, 'pady':2, 'anchor':W}
        self.rb_value = tk.BooleanVar(value=True) 
        self.rb_1 = ttk.Radiobutton(self, 
            variable=self.rb_value, 
            value=True,
            text='km_to_mi'
        )
        self.rb_1.pack(**options)

        self.rb_2 = ttk.Radiobutton(self, 
            variable=self.rb_value, 
            value=False,
            text='mi_to_km'
        )
        self.rb_2.pack(**options)

class View(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=1, pady=2, fill=BOTH, expand=True)

        # contant
        self.label = ttk.Label(self, text='Converter')
        self.label.pack()

        self.set_frame = SetFrame(container)
        self.set_frame.rb_1['command'] = self.switch_win
        self.set_frame.rb_2['command'] = self.switch_win

        win_first = WinFirst(self)
        win_second = WinSecond(self)
        self.list_win = []
        self.list_win.append(win_first)
        self.list_win.append(win_second)
        self.list_win[1].forget()

    def switch_win(self):
        if self.set_frame.rb_value.get():
            self.list_win[1].forget()
            self.list_win[0].pack(padx=2, pady=2, fill=BOTH, expand=True)
        else:
            self.list_win[0].forget()
            self.list_win[1].pack(padx=2, pady=2, fill=BOTH, expand=True)

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def convert(self, x):
        try:
            self.model.value = x
            if self.view.set_frame.rb_value.get(): 
                print('1')
                res = self.model.km_to_mi()
                self.view.list_win[0].set_full_result(x, res)
            else:
                print('2')
                res = self.model.mi_to_km()
                self.view.list_win[1].set_full_result(x, res)

        except TypeError as error:
            print(error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world!')
        self.geometry('300x400')
        #self.resizable(False, False)
        
        view = View(self)
        model = Model(10)

        controller = Controller(view, model)

        view.list_win[0].set_controller(controller)
        
        view.list_win[1].set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
