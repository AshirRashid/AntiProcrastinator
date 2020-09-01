from ttkthemes import ThemedTk
from tkinter.ttk import Frame, Style, Label, LabelFrame, Spinbox, Radiobutton, Entry, Button
from tkinter import IntVar, messagebox
from task import Task
import datetime
import time
import pickle

class Page1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.style = Style()

        self.time_frame = LabelFrame(self, text='Time Setting')
        self.hour_label = Label(self.time_frame, text='Hours')
        self.hour_box = Spinbox(self.time_frame, from_=0,  to=24)

        self.minute_label = Label(self.time_frame, text='Minutes')
        self.minute_box = Spinbox(self.time_frame, from_=0,  to=60)

        self.second_label = Label(self.time_frame, text='Seconds')
        self.second_box = Spinbox(self.time_frame, from_=0,  to=60)

        self.break_label = Label(self.time_frame, text='Time During Sessions')
        self.break_var = IntVar()
        self.break_var.set(4)
        self.break_radio_button_3 = Radiobutton(self.time_frame, text='3 min', variable=self.break_var, value=3)
        self.break_radio_button_4 = Radiobutton(self.time_frame, text='4 min', variable=self.break_var, value=4)
        self.break_radio_button_5 = Radiobutton(self.time_frame, text='5 min', variable=self.break_var, value=5)
        self.break_radio_button_6 = Radiobutton(self.time_frame, text='6 min', variable=self.break_var, value=6)
        self.break_radio_button_7 = Radiobutton(self.time_frame, text='7 min', variable=self.break_var, value=7)

        self.name_label = Label(self.time_frame, text='Task Name')
        self.name_entry = Entry(self.time_frame)

        self.reminder_label = Label(self.time_frame, text='Reminder')
        self.reminder_entry = Entry(self.time_frame)

        self.generate_button = Button(self, text='Generate Task', command=self.create_task)
        self.save_button = Button(self, text='Save Configuration', command=self.save_config)
        self.load_button = Button(self, text='Load Configuration', command=self.load_config)
        self.clear_button = Button(self, text='Clear', command=self.clear)


        # GRIDDING OPERATIONS
        self.hour_label.grid(row=1, column=0)
        self.hour_box.grid(row=1, column=1)
        self.minute_label.grid(row=1, column=2)
        self.minute_box.grid(row=1, column=3)
        self.second_label.grid(row=1, column=4)
        self.second_box.grid(row=1, column=5)

        self.break_label.grid(row=2, column=0)
        self.break_radio_button_3.grid(row=2, column=1)
        self.break_radio_button_4.grid(row=2, column=2)
        self.break_radio_button_5.grid(row=2, column=3)
        self.break_radio_button_6.grid(row=2, column=4)
        self.break_radio_button_7.grid(row=2, column=5)

        self.name_label.grid(row=3, column=0)
        self.name_entry.grid(row=3, column=1, columnspan=5, sticky='ew')
        self.reminder_label.grid(row=4, column=0)
        self.reminder_entry.grid(row=4, column=1, columnspan=5, sticky='ew')

        self.generate_button.grid(row=1, column=0, sticky='snew')
        self.save_button.grid(row=2, column=0, sticky='snew')
        self.load_button.grid(row=3, column=0, sticky='snew')
        self.clear_button.grid(row=4, column=0, sticky='snew')

        self.time_frame.grid(row=0, column=0)
        self.grid(row=0, column=0)

    def create_task(self):
        # Task signature: (task_name, task_duration, break_duration, task_reminder=None)
        hours = self.hour_box.get()
        minutes = self.minute_box.get()
        seconds = self.second_box.get()
        break_time = self.break_var.get()
        if hours and seconds and minutes:
            total_time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
            return Task(self.name_entry.get(), total_time, break_time)
        elif hours == 's':
            return Task('sample task', 5, 3/60)

    def save_config(self):
        with open('config.pickle', 'wb+') as config:
            pickle.dump(self.create_task(), config)

    def load_config(self):
        with open('config.pickle', 'rb') as config:
            unpickled_task = pickle.load(config)
            Task.tasks.append(unpickled_task)

    def clear(self):
        self.name_entry.delete(0, 'end')
        self.reminder_entry.delete(0, 'end')
        self.hour_box.set('')
        self.minute_box.set('')
        self.second_box.set('')




if __name__ == '__main__':
    root = ThemedTk()
    test = Page1(root)
    test.grid(row=0, column=0)
    root.mainloop()