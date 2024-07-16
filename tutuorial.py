import tkinter as tk
from tkinter import ttk
from ctypes import windll
from click_game import click_me



root = tk.Tk()
root.title('The Game Corner')
root.geometry('600x400+50+50')
root.resizable(False, False)

#create label
message = ttk.Label(root, text="Hello, Player!")
message.pack()
message2 = ttk.Label(root, text="Let's play a game!")
message2.pack()

#click me button


click_me_button = ttk.Button(
    root,
    text="click me",
    command=click_me
)

click_me_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

def callback():
    print("HEllo World")

game_1_button = ttk.Button(
   root, 
   text="Game 1", 
   command=callback
)

game_1_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
#address the blur
windll.shcore.SetProcessDpiAwareness(1)

#keep window open
root.mainloop()