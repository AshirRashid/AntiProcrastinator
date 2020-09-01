from concurrent.futures import ThreadPoolExecutor
from tkinter.ttk import Style, Label, Frame, Button
from tkinter import messagebox, Canvas
from ttkthemes import ThemedTk
from task import Task
import datetime
import tkinter
import time
from pygame import mixer
from math import floor
import os

mixer.init()

class Page2(Frame):
    '''Note: the canvas used is from tkinter but the rest of the widgets are from ttk
    '''
    def __init__(self, master):
        Frame.__init__(self, master)
        self.style = Style()
        self.style.configure('TimeLabel.TLabel', font=('default', 120))
        self.style.configure('Specifier.TLabel', font=('default', 20))
        self.timer = 'initialized'
        self.master = master
        self.break_start = -1
        self.start_timer_button = Button(self, text='Start Timer', command=self.start_timer)
        self.time_display_label = Label(self, style='TimeLabel.TLabel')
        self.task_or_break = Label(self, text='Task', style='Specifier.TLabel')
        self.start_timer_button.pack(fill='x', anchor='n', expand=True)
        self.task_or_break.pack(fill='x', anchor='n', expand=True)
        self.time_display_label.pack(fill='both', anchor='center', expand=True)

    def clock_function(self, time_duration):
        hours = floor(time_duration / 3600)
        minutes = floor((time_duration - hours * 3600) / 60)
        seconds = time_duration - hours * 3600 - minutes * 60

        self.time_display_label.configure(text=f'{hours:02}: {minutes:02}: {seconds:02.0f}')

        difference = time.time() - self.start
        self.start = time.time()
        print(difference)
        time_duration -= difference
        if time_duration <= 0:
            self.bell()
            self.break_start *= -1
            if self.break_start == 1:
                mixer.music.play(start=1)
                messagebox.showinfo('Stop', "The time for the Task has elapsed. It's time to relax.")
                mixer.music.stop()
                self.start = time.time()
                time_duration = Task.tasks[-1].break_duration
                self.task_or_break.configure(text='Break')
            else:
                mixer.music.play(start=1)
                messagebox.showinfo("Stop", "The time for the break is over. Get back to work.")
                mixer.music.stop()
                self.start = time.time()
                time_duration = Task.tasks[-1].task_duration
                self.task_or_break.configure(text=f'Task: {self.current_task.task_name}')
        
        self.timer = self.after(1000, self.clock_function, time_duration)

    def start_timer(self):
        '''
        Cancels the previously running clock_function
        '''
        sound_file = None
        for i in os.listdir():
            if i.endswith('.mp3'):
                if i.startswith('song'):
                    pass
                else:
                    sound_file = i
        if sound_file:
            mixer.music.load(sound_file)
        else:
            mixer.music.load('song.mp3')
        self.start = time.time()
        if Task.tasks:
            self.after_cancel(self.timer)
            self.current_task = Task.tasks[-1]
            self.task_or_break.configure(text=f'Task: {self.current_task.task_name}')
            self.clock_function(self.current_task.task_duration)
        else:
            messagebox.showerror('No Task Supplied', 'Please create a task first.')
if __name__ == '__main__':
    import os
    for i in os.listdir():
        if i.endswith('.mp3'):
            if i.startswith('song'):
                print('that')
