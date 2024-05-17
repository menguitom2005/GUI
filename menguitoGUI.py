import tkinter as tk

from tkinter import messagebox 3

Function to display a message box with the confession

def confess():

confession entry.get()

if confession

 messagebox.showinfo("Confession', 'You are my secret crushinin(confession)")

else

messagebox showinfo("Confession", "Please enter your confession first")

Create the man window

rool tk Tk()

root.title('Secret Crush Confession)

#Label for the instruction

label tk Label(root, text="Confess your feelings to your secret crush:")

label.pack()



# Entry field for entering the confession

entry tk. Entry(root, width=50)

entry.pack()



#Button to confess

25 button tk Button(root, text="Confess", command confess)

button.pack()

#Start the GUI event loop

root mainloop
