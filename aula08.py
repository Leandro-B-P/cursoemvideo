#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {} m corresponde a {:.0f} cm e {:.0f} mm'.format(medida, cm, mm))
