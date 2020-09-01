from tkinter.ttk import Notebook, Label, Frame, Style
from ttkthemes import ThemedTk
from tkinter import messagebox
from page2 import Page2
from page1 import Page1
from page3 import Page3
from task import Task
import datetime
import logging
import tkinter
import time

class PomodoroNotebook(ThemedTk):
    def __init__(self):
        ThemedTk.__init__(self)
        self.iconbitmap('pomodoro_icon.ico')
        self.resizable(False, False)
        self.set_theme('radiance')
        self.style = Style()
        self.style.configure('.', font=('Times', 13), takfocus=0, xpad=10)
        self.style.configure('TFrame', background='#471d0f')
        self.style.configure('TButton', 'Button.focus'=={'sticky': '0'})
        print(self.style.layout('TButton'))
        self.title('Pomodoro')
        self.protocol("WM_DELETE_WINDOW", self.quit_event)

        self.note = Notebook(self)
        self.page_one = Page1(self.note)
        self.page_two = Page2(self.note)
        self.page_three = Page3(self.note)

    def batch_grid(self):
        self.note.add(self.page_one, text='Task Generation')
        self.note.add(self.page_two, text='Current Task')
        self.note.add(self.page_three, text='History')
        
        self.note.pack(fill='both')
        self.mainloop()

    def quit_event(self):
        try:
            pass
        except Exception as error:
            logging.debug(error)
        finally:
            self.destroy()

if __name__ == '__main__':
    root = PomodoroNotebook()
    root.batch_grid()
    
