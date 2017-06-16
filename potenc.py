#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com


def potecia(x):
    quadrado = x**2 # Retorna o valor de 'X' ao quadrado
    cubo = x**3 # Retorna o valor de 'X' elevado ao cubo

    return quadrado, cubo # Retorno da função

q, c = potecia(10) # Retorno multiplo
print(q)
print(c)
