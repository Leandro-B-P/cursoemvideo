#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com
import car

Carro1 = car.Carro(2017, 'Astra', 'Preto', 'Hatchi')

Carro1.abastecer()

print("O carro é do ano: {} ".format(Carro1.ano))
print("O carro é da cor: {}".format(Carro1.cor))
print("O carro é do modelo: {}".format(Carro1.modelo))
print("O carro é da marca: {}".format(Carro1.marca))
