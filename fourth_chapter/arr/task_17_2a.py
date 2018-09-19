#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os.path
from sys import argv
from task_17_1 import read_file
from task_17_2 import parse_sh_cdp_neighbors
import glob
from pprint import pprint
import yaml

'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''

def create_dict_cdp(list_dict):
    dict_cdp = dict()
    for idict in list_dict:
        dict_cdp.update(idict)

    return dict_cdp

if __name__ == "__main__":
    args = glob.glob('sh_cdp*.txt')
    pprint(create_dict_cdp([parse_sh_cdp_neighbors(read_file(ifile)) for ifile in args]))

