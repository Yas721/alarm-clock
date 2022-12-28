from tkinter import *
import datetime 
from tkinter.messagebox import *
from tkinter.ttk import *
import winsound

w=Tk()
w.geometry('400x200')
l1=Label(w,text='HOURS:')
l1.grid(row=0,column=0)
l2=Label(w,text='MINUTES:')
l2.grid(row=1,column=0)
w.title('alarm clock')



def alarm():

    if c1.get()=='am':
       x=int(e1.get())
       y=int(e2.get())
    elif c1.get()=='pm':
        x=int(e1.get())+12
        y=int(e2.get())

   
    showinfo('notificarion','alarm has been set')
    while True:
        if x==datetime.datetime.now().hour and y==datetime.datetime.now().minute:
            for i in range(0,100):
                winsound.Beep(10000, 100)
            break
    

e1=Entry(w)
e2=Entry(w)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(w,text='set alarm',command=alarm)
b1.grid(row=2,column=1)
c1=Combobox(w,values=['am','pm'])
c1.grid(row=0,column=2)

w.mainloop()