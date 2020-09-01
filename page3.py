from ttkthemes import ThemedTk
from tkinter import messagebox, Canvas
from tkinter.ttk import Frame, Style, Label, Scrollbar, Button, LabelFrame
from task import Task
import datetime
import tkinter
import time

class Page3(Frame):
    '''Note: the canvas used is from tkinter but the rest of the widgets are from ttk
    '''
    def __init__(self, master):
        Frame.__init__(self, master)
        self.style = Style()
        self.style.configure('TButton', takefocus=0)
        
        self.canvas = Canvas(self, background='#471d0f')
        self.scroll_history = Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.moving_frame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.moving_frame, anchor='nw')
        self.moving_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.configure(yscrollcommand=self.scroll_history.set)

        self.update_button = Button(self.moving_frame, text='Update History', command=self.update_history)

        self.scroll_history.pack(fill='both', side='right')
        self.canvas.pack(fill='both', side='left', expand=True)
        self.update_button.pack(anchor='ne', fill='x', expand=True)
        # Label(self.moving_frame, text='HISTORY HERE').pack(anchor='ne', fill='x')
        self.grid(row=0, column=0)

    def update_history(self):
        if Task.tasks:
            for task in Task.tasks:
                if task.on_display == False:
                    history_instance = LabelFrame(self.moving_frame, text=task.task_name)
                    Label(history_instance, text=f'Task Duration: {datetime.timedelta(seconds=task.task_duration)}').pack()
                    Label(history_instance, text=f'Break Duration: {task.break_duration}').pack()
                    Label(history_instance, text=f'Made on: {task.init_date}').pack()
                    history_instance.pack(anchor='n', fill='both')
                    task.on_display = True
if __name__ == '__main__':
    pass