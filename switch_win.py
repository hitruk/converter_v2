
# 1. switch frame
# 2. Создать два фрейма WinFirst, WinSecond которые будут переключаться в виджете LabelFrame

import tkinter as tk
from tkinter.constants import *
from tkinter import ttk


class WinFirst(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=1, pady=2, fill=BOTH, expand=True)

        # contant
        self.label = ttk.Label(self, text='Win First')
        self.label.pack()

class WinSecond(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=1, pady=2, fill=BOTH, expand=True)

        # contant
        self.label = ttk.Label(self, text='Win Second')
        self.label.pack()

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

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world!')
        self.geometry('300x400')
        #self.resizable(False, False)

        view = View(self)


if __name__ == '__main__':
    app = App()
    #view = View(app)
    # win_first = WinFirst(view)
    # win_second = WinSecond(view)
    # set_frame = SetFrame(app)
    app.mainloop()
