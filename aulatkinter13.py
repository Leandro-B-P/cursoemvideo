# coding: utf8
from tkinter import *

janela = Tk()
lb = Label(janela, text='Oi galera!!')
lb.place(x=100, y=100)


# wxh+1+t

janela.geometry('300x300+200+200')
janela.mainloop()