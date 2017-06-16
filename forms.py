#!/usr/bin/python3
# -*- coding: utf-8 _-*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com


def login(usuario='root', senha='toor'):
    user = input('Digite o usuario: ')
    passwd = input('Digite a senha: ')
    if user == usuario and passwd == senha:
        print('Parabens acesso garantido {}!'.format(user))
    else:
        print('Desculpe mais o usuario {} não esta cadastrado!'.format(user))



login()
