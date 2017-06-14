#from pyautogui import *#
from tkinter import ttk
from tkinter import *
import time
import ctypes
import sys
import os

root = Tk()
root.title('AutoClicks')
file_settings = open('data.txt', 'r+')
num_of_clicks = file_settings.readline()
file_settings.close()

mouse = ctypes.windll.user32
state = False

file_settings_cps = open('data.txt', 'r+')
cps = int(file_settings_cps.readline())
file_settings_cps.close()



def StateFalse(self):
    global state
    global x
    if state == True:
        state = False
        x = 0
        print('False')

def StateTrue(self):
     global state
     global x
     if state == True:
        state = True
     else:
        x = 0
        state = True
        print('True')

def popupmsg():
    def change_num_of_clicks():
        with open("data.txt", "w") as settings:
            num = new_num.get()
            time.sleep(2)
            settings.write(num)
            settings.close()
            print('It Worked!!!')
            print(settings.closed)
    popup = Tk()
    popup.wm_title("!")
    popup.geometry('300x300')
    label = Label(popup, text="New num of clicks per second")
    new_num = Entry(popup)
    button1 = Button(popup, text="Activate", command=change_num_of_clicks)
    button1.pack()
    new_num.pack()
    label.pack()
    popup.mainloop()

def close():
    sys.exit(0)


timekeeper = 0
x = 0

mainframe = ttk.Frame(root)
mainframe.grid(padx=5, pady=5)

startButton = ttk.Button(mainframe, text="Start", width=30, command=StateTrue).pack()
stopButton = ttk.Button(mainframe, text="Stop", width=30, command=StateFalse).pack()
button = ttk.Button(mainframe, text='Change num of clicks',width=30, command=popupmsg).pack()
close = ttk.Button(mainframe, text='Close', width=30, command=close).pack()


root.bind("<F1>", StateTrue)
root.bind("<F3>", StateFalse)

while True:
    timekeeper += 1
    if state == True:
        print('State True')

        print(state)
        time.sleep(cps / 1000)
        mouse.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
        mouse.mouse_event(4, 0, 0, 0, 0)  # left mouse button up
        x += 1
    root.update()
