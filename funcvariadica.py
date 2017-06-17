#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista Pereira
# e-mail: leandrobatistapereira98@gmail.com


def lista_de_argumentos(*args):
    print(args)


def lista_de_parametros_associativos(**kwargs):
    print(kwargs)


def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

argumentos(1,2,3,4,5, um=1,dois=2,tres=3,quatro=4,cinco=5)
lista_de_argumentos(1,2,3,4,5,6,7)
lista_de_parametros_associativos(a=1, b=2, c=3, d=4)
lista_de_parametros_associativos(um=1, dois=2, tres=3, quatro=4)