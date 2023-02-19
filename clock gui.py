from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    TimeVar = time.strftime("%I:%M:%S %p")
    Clock.config(text=TimeVar)
    Clock.after(200,get_time)

Clock = Label(master, font =("Calbri",90),bg="yellow",fg="blue")
Clock.pack()

get_time()

master.mainloop()