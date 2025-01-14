from tkinter import *

window=Tk()
window.title('Welcome to my tkinter window')
window.geometry('400x300')

lbl=Label(text="hello",bg='blue',fg='white')
btn=Button(text='Click',bg='black',fg='white')
entry=Entry(bg='blue',fg='white',width=40)
tbox=Text(bg='green',fg='white',width=40)

fram=Frame(master=window,relief=GROOVE,borderwidth=6)
l1=Label(master=fram,text='hello')

lbl.pack()
btn.pack()
entry.pack()
tbox.pack()
fram.pack()
l1.pack()

window.mainloop()