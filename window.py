#!/usr/bin/python3
# -*- coding: utf-8 _-*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

import tkinter

janela = tkinter.Tk()
janela.title('Janela 1')

janela['bg']    = 'red'
janela['background'] = 'red'

janela.geometry('300x300+100+100')

janela.mainloop()
