# from tkinter import *

# new_window = ''
# def openMain():
#     global new_window
#     new_window = Toplevel(root)
#     new_window.geometry("250x250")
#     new_window.title("New Window")
#     new_window.resizable(False, False)
#     lbl = Label(new_window, text='I am a new window')
#     lbl.pack()
#     btn2 = Button(new_window, text='Close Me', command=lambda: new_window.destroy())
#     btn2.pack()
#
# root = Tk()
#
# lbl = Label(new_window, text='Customer Delivery App')
# lbl.pack()
# bt = Button(root, text='Enter new customer', command=openMain)
# bt.pack(padx=10, pady=10)
# bt = Button(root, text='Distance Details', command=openMain)
# bt.pack(padx=10, pady=10)
# bt = Button(root, text='Sentiment Details', command=openMain)
# bt.pack(padx=10, pady=10)
#
# Button(root, text='Close Newly Opened Window', command=lambda: new_window.destroy()).pack()
#
# root.geometry("500x500")
# root.title('Main Window')
# root.mainloop()
from tkinter import font

from windowPrompt3 import Window


w = Window()
# # w.inputCustomer()
w.mainWindow()


# import tkinter
# from tkinter_custom_button import TkinterCustomButton
#
# app = tkinter.Tk()
# app.geometry("300x200")
# app.title("TkinterCustomButton")
#
# # def button_function():
# #     print("Button pressed")
# buttonFont = font.Font(family='Century Gothic', size=11)
# button_1 = TkinterCustomButton(text="My Button", corner_radius=10, text_font=buttonFont)
# button_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
# app.mainloop()



# import pyautogui,time
#
# f=open('death note.txt','r')
# time.sleep(3)
# for word in f:
#     pyautogui.typewrite(word)
#
# print('lol')