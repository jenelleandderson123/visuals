from tkinter import *
root = Tk()
root.title("number pad")
root.geometry('300x500')

num =[[9, 8, 7,],[6, 5, 4],[3, 2, 1],['#',0,'*']]

for i in range(4):
    root.columnconfigure(i, weight = 1, minsize=75)
    root.rowconfigure(i, weight = 1, minsize=50)
    for j in range(0, 3):
        frame = Frame(
            master = root,
            relief = RAISED,
            borderwidth = 1,

        )
        frame.grid(row = i, column=j)
        label = Label(master = frame, text = num[i][j],bg = 'red') 
        label.pack(padx = 3, pady = 3)

root,mainloop()