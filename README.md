# AntiProcrastinator
This is my tkinter(python3) implementation of the pomodoro technique.

It is based on the tkitner.ttk widget, Notebook.

Page1:
  
  Input: Time for the task, time for the break, task name. The reminder field does nothing(yet).
  
  Output: It makes a Task(my own class) object with the input the user passes in.

Page2:
  
  Input: The most resent task created by the user in the in Page1 is used
  
  Output: Using the task time, break time and task name stored in the Task object, a timer is started. When the time for a task or a break ends, the music starts. A pop up appears and when it is closed, the music ends.
  
  Additional Info: You need to place a .mp3 file in the current dir or it will resort to using the song.mp3 file. If it does not find any .mp3 file, the program will crash.
  
  An attempt to make the clock as accurate as possible(not relying on the assumption that the processing in every frame would take no time) resulted in a problem in the diplay(skipping some seconds in between) since the clock is not in sync with the main loop.
  
Page3:
  
  Input: The input consists of the task created in this session(which starts when you run the app).

  Output: The output shows information related to the tasks input
  
  Additional Info: To show a longer history, I was thinking of using a pickle file as a FIFO queue.

Notebook:
   
   Brings everything together. Adds the pages to a tkinter.ttk.Notebook.
