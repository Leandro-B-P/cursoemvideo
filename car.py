#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com


class Carro:
    ano = ""
    cor = ""
    marca = ""
    modelo = ""

    def __init__(self, ano, cor, marca, modelo):
        self.ano = ano
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def andar(self):
        print("O carro esta em movimento")

    def abastecer(self):
        print("Veiculo abastecido")
