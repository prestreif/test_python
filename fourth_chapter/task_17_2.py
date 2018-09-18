#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re
from sys import argv
from task_17_1 import *
import argparse

'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

def parse_sh_cdp_neighbors(output):
    dict_neig = {re.search('(.*?)>sho?w? cdp ', output).group(1): None}
    print(dict_neig)

#list(re.search('(\S+)\s+(\S+\s\S+).*\s(\S+\s\S+)', val).groups() for val in re.sub('.*[^\d]\n', '',  str_file, re.DOTALL).strip().split('\n'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="parser show cdp neighbors")

    parser.add_argument('file_name', action="store", help="file name with output show cdp neighbor")

    args = parser.parse_args()

    parse_sh_cdp_neighbors(read_file(args.file_name))
    #print(read_file(args.file_name))
