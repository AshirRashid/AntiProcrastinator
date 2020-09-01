from ttkthemes import ThemedTk
from tkinter import messagebox
from tkinter import ttk
import datetime, time
import tkinter
import inspect

class Task():
    id_start = 0
    clock = True
    tasks = []
    def __init__(self, task_name, task_duration, break_duration, task_reminder=None):
        self.init_date = datetime.datetime.now().date()
        self.on_display = False
        self.task_name = task_name
        self.task_duration = task_duration
        self.break_duration = break_duration * 60

        if task_reminder:
            self.task_reminder = task_reminder
        else:
            self.task_reminder = f'The Time Dedicated for {self.task_name} has Elapsed.'

        Task.id_start += 1
        Task.tasks.append(self)

if __name__ == '__main__':
    print(inspect.signature(Task))