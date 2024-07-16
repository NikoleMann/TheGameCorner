import tkinter as tk
from tkinter import ttk
from ctypes import windll
from click_game import click_me


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # labels are messages printed to the frame
        message = ttk.Label(self, text="Hello, Player!")
        message.pack()
        message2 = ttk.Label(self, text="Let's play a game!")
        message2.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        click_me_button = ttk.Button(
        self,
        text="click me game",
        command=click_me
)

        click_me_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

        # show the frame on the container
        self.pack(**options)

    def button_clicked(self):
       pass
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('My Awesome App')
        self.geometry('600x400')


if __name__ == "__main__":
    #address the blur
    windll.shcore.SetProcessDpiAwareness(1)
    app = App()
    frame = MainFrame(app)
    app.mainloop()