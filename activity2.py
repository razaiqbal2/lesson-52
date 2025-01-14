from tkinter import *
 
window=Tk()
window.title('tkinter grid')


for i in range(3):
    for j in range(3):
        fame=Frame(master=window,
                   relief=GROOVE,
                   borderwidth=4)
        fame.grid(row=i,column=j,padx=3,pady=3)
        l=Label(master=fame,text='row {}\n column{}'.format(i,j))
        l.pack()

window.mainloop()
