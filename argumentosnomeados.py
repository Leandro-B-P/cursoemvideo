#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com


def dados_pessoais(nome, sobrenome, idade, sexo):
    print('Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}'
          .format(nome, sobrenome, idade, sexo))


dados_pessoais(nome='Leandro', sobrenome='Batista',
               idade=32, sexo='Masculino')
