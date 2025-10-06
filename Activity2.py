# Create a virus scanner simulation with pop-up alert using tkinter
# You will learn to use message box to diplay warning box understand button command and create interact alert system for application
# Virus detected alert using tkinter
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
# Function for displaying warning message
# This will be called once the button is clicked
# Messagebox.showwarning("window name",text to display)
def msg():
    messagebox.showwarning("Alert","Stop! Virus Found")
# Adding button widget to windows
button = Button(root,text = "scan for virus", command = msg)
button.place(x = 50, y = 80)
root.mainloop()