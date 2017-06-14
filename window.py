#encoding: utf8

import tkinter

janela = tkinter.Tk()
janela.title('Janela 1')

janela['bg']    = 'red'
janela['background'] = 'red'

janela.geometry('300x300+100+100')

janela.mainloop()
