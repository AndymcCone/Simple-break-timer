from tkinter import *
from tkinter import ttk
import time
import pygame
from pygame import mixer

mixer.init()

def display_text():
    mixer.music.stop()
    global entry
    try:
        string = int(entry.get())
        for sekunti in range(string, -1, -1):
            sekunnit = sekunti % 60
            minuutit = int(sekunti / 60) % 60
            tunnit = int(sekunti / 3600)
            teksti = (f"{tunnit:02}:{minuutit:02}:{sekunnit:02}")
            label.configure(text=teksti)
            window.update()
            time.sleep(1)
        mixer.music.load("alarm.mp3")
        mixer.music.play()
    except:
        label.configure(text="Use only positive integers")
        window.update()

def increase():
    pass

def exit_program():
    window.destroy()



window = Tk()
window.title("Simple break timer")

label=Label(window, text="Enter time in seconds: ", font=('Arial',10))
label.grid(row=0, column=0, columnspan=2)

entry = Entry(window, width= 40,borderwidth=5)
entry.focus_set()
entry.grid(row=1, column=0, columnspan=2)

ttk.Button(window, text = "Start",width = 20, command = display_text).grid(row=2, column=0, pady=5)
ttk.Button(window, text = "Close", width = 20, command = exit_program).grid(row=2, column=1, pady=5)
window.mainloop()