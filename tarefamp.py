#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

name = input('Digite seu nome: ')
passwd = input('Digite sua senha : ')
if name.capitalize() == 'Mary':
    if passwd == 'password':
        print('Hello {} acess garanted!'.format(name))
    else:
        print('Acess Denied {}!'.format(name))
