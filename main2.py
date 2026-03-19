from tkinter import *

root = Tk()
root.title("Login App")
root.geometry('300x500')

frame = Frame(master = root, height = 200, width = 350, bg = 'blue')
lbl1 = Label(frame, text = "Full Name", bg = "red", fg = "black", width = 12)
lbl2 = Label(frame, text = "Name ID", bg = "red", fg = "black", width = 12)
lbl3 = Label(frame, text = "Enter passcode", bg = "red", fg = "black", width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = "*")

def display():
    name = name_entry.get()
    greet = "Hey " + name
    message ="\n Congratulations for your new account!"
    textbox.insert(END,greet)
    textbox.insert(END, message)

textbox = Text(bg = 'white', fg = 'black')

btn = Button(text = "Create Account", command = display, bg = 'red')

frame.place(x = 20, y = 0)
lbl1.place(x =20, y = 80)
name_entry.place(x= 150, y = 80)

lbl2.place(x= 20, y = 80)
email_entry.place(x= 150, y = 140)

lbl3.place(x= 20, y = 140)
pass_entry.place(x= 150, y = 140)

btn.place(x= 130, y = 218)

textbox.place(y = 250)

root.mainloop()