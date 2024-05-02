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

# image = PhotoImage(file="python-logo.png")

# width, height = 100, 100  # Set your desired width and height
# image = image.subsample(image.width() // width, image.height() // height)

# label = Label(window, text="Hello Python", image=image, compound="bottom")
# label.pack()

# label.image = image  # Keep a reference to the image to prevent garbage collection
# label.config(anchor=CENTER)

# window.mainloop()

# buttons 🛎️
# def button_click():
#     print("Button clicked!")

# window = Tk()
# window.geometry("200x100")
# window.title("Click Me Button")

# button = Button(window, text="Click Me", command=button_click)
# button.pack(pady=20)

# window.mainloop()

# entry ⌨️
# def submit():
#     input_text = entry.get()
#     print("Submitted text:", input_text)
#     # You can perform any action with the input_text here, like processing it or displaying it in another widget

# window = Tk()
# window.geometry("300x150")
# window.title("Entry Box and Submit Button")

# # Entry box
# entry = Entry(window, width=30)
# entry.pack(pady=10)

# # Submit button
# submit_button = Button(window, text="Submit", command=submit)
# submit_button.pack()

# window.mainloop()

# checkbutton ✔️
# def show_selection():
#     if var.get() == 1:
#         print("Check button is selected")
#     else:
#         print("Check button is not selected")

# window = Tk()
# window.geometry("300x150")
# window.title("Check Button")

# # Check button variable
# var = IntVar()

# # Check button
# check_button = Checkbutton(window, text="Check me", variable=var)
# check_button.pack()

# # Button to show selection
# show_button = Button(window, text="Show Selection", command=show_selection)
# show_button.pack(pady=10)

# window.mainloop()

# radiobuttons 🔘
# def show_selection():
#     print("Selected food:", var.get())

# window = Tk()
# window.geometry("300x200")
# window.title("Radio Buttons")

# # Array of food items
# foods = ["Pizza", "Burger", "Sushi", "Tacos"]

# # IntVar to track the selected food
# var = IntVar()

# # Create radio buttons for each food item
# for food in foods:
#     radio_button = Radiobutton(window, text=food, variable=var, value=food)
#     radio_button.pack(anchor=W)

# # Button to show selection
# show_button = Button(window, text="Show Selection", command=show_selection)
# show_button.pack(pady=10)

# window.mainloop()