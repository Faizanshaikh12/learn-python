from tkinter import *

# windows 🖼️
# widgets =  GUI elements: buttons, textboxes, labels, images
# windows = Serves as a container to hold or contain these widgets

window = Tk(); #instantiate an instance of window
window.geometry("420x420")

window.title("My First Tkinter Program")

icon = PhotoImage(file='python-logo.png')
window.iconphoto(True, icon)

window.config(background="#5C5CFF")

window.mainloop() # place window on computer screen. listen for evetns
