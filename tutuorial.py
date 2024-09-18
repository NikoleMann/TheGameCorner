import tkinter as tk
from tkinter import ttk
from tkinter import *
from ctypes import windll
from click_game import openNewWindow



root = tk.Tk()
root.title('The Game Corner')
root.geometry('600x400+50+50')
root.resizable(False, False)

#create label
message = ttk.Label(root, text="Hello, Player!")
message.pack()
message2 = ttk.Label(root, text="Let's play a game!")
message2.pack()

#selection frame
frame = LabelFrame(root, text="Choose your game:", padx=10, pady=10)
frame.pack(padx=15, pady=15)
#click me button
click_game_button = ttk.Button(
    frame,
    text="clicker game",
    command=openNewWindow
)

click_game_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#address the blur
windll.shcore.SetProcessDpiAwareness(1)

#keep window open
root.mainloop()