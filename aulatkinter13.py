#!/usr/bin/python3
# -*- coding: utf-8 _-*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

from tkinter import *

janela = Tk()
lb = Label(janela, text='Oi galera!!')
lb.place(x=100, y=100)


# wxh+1+t

janela.geometry('300x300+200+200')
janela.mainloop()
