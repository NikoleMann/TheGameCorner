from tkinter import *
from tkinter import ttk

 

def openNewWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    global newWindow, label, num 
    num = 0
    newWindow = Toplevel()
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow, 
          text ="This is the clicker game").pack()
    
    click_me_button = ttk.Button(
    newWindow,
    text="click me",
    command=click_me
)

    click_me_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # Initial label to display the count
    label = Label(newWindow, text=num)
    label.pack()  # Pack it initially

def click_me():
    global num
    num += 1
    label.config(text=num) #updates the label's text