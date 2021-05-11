# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("800x600")


# Change the label text
def show():
    label.config(text='\n'+clicked.get())


# Dropdown menu options
options = []
for i in range(5):
    options.append('Customer '+str(i+1))

# options = [
#     "Customer "+str(1),
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday"
# ]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set(options[0])

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(root, text="Update Page", command=show).pack()

# Create Label/String to be attached
label = Label(root, text="\nHello")
label.pack()

# Execute tkinter
root.mainloop()