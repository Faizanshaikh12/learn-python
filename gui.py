from tkinter import *

# windows 🖼️
# widgets =  GUI elements: buttons, textboxes, labels, images
# windows = Serves as a container to hold or contain these widgets

# window = Tk(); #instantiate an instance of window
# window.geometry("420x420")

# window.title("My First Tkinter Program")

# icon = PhotoImage(file='python-logo.png')
# window.iconphoto(True, icon)

# window.config(background="#5C5CFF")

# window.mainloop() # place window on computer screen. listen for evetns

# labels 🏷️
# window = Tk()

# # Load the image
# image = PhotoImage(file="python-logo.png")

# # Resize the image to desired dimensions
# width, height = 100, 100  # Set your desired width and height
# image = image.subsample(image.width() // width, image.height() // height)

# # Create a label with both text and image
# label = Label(window, text="Hello Python", image=image, compound="bottom")
# label.pack()

# # Center the image within the label
# label.image = image  # Keep a reference to the image to prevent garbage collection
# label.config(anchor=CENTER)

# window.mainloop()