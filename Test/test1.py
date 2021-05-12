# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("800x600")
root.title('Customer Delivery Details')

# Change the label text
def show(*args):
    getIndex = options.index(clicked.get())
    label2.config(text="\nDistance between 2 points :\t" + optionsFee[getIndex])
    labelTime.config(text="\nTime taken :\t" + optionsFee[getIndex])


# Dropdown menu options
options = []
for i in range(5):
    options.append('Customer '+str(i+1))

optionsFee = []
for i in range(5):
    optionsFee.append('Customer Fee '+str(i+1))

header = Label(root, text="Customer Delivery Details\n\nSelect Customer Number")
header.config(font=('Times', 14))
header.pack()

# Create Dropdown menu
clicked = StringVar(value="Select a hub")
clicked.trace("w", show)
drop = OptionMenu(root, clicked, *options)
drop.pack()


# Create Label/String to be attached
label = Label(root, text="\nCalculate distance between 2 points")
label.pack()
label2 = Label(root, text="\nDistance between 2 points :\t--")
label2.pack()
labelTime = Label(root, text="\nTime taken :\t--")
labelTime.pack()


# CREATE HUB DROPDOWN
label3 = Label(root, text="\n\nSELCECT CUSTOMER HUB")
label3.pack()
# Change the label text


# Dropdown menu options
optionsHub = [
        'City-link Express',
        'Pos Laju',
        'GDEX',
        'J&T',
        'DHL'
]

# initial menu text
# clicked1.set('Select a hub')
def showHub(*args):
    getIndex = optionsHub.index(clicked1.get())
    labelHub.config(text="\nDistance between 3 points :\t" + optionsHub[getIndex])
    labelTime2.config(text="\nTime taken :\t")

clicked1 = StringVar(value="Select a hub")
clicked1.trace("w", showHub)

# Create Dropdown menu
drop1 = OptionMenu(root, clicked1, *optionsHub)
drop1.pack()
labelHub = Label(root, text="\nDistance between 3 points :\t--")
labelHub.pack()
labelTime2 = Label(root, text="\nTime taken :\t--")
labelTime2.pack()


# Execute tkinter
root.mainloop()