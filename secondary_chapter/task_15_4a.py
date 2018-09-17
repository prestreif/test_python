#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re
import argparse
from sys import argv

parser = argparse.ArgumentParser(description="parser 'sh ip int br' with file_name")

parser.add_argument('file_name', action="store", help="file_name with output command sh ip int br")

args = parser.parse_args()

headers = ['interface', 'address', 'status', 'protocol']

def parse_sh_ip_int_br(file_name):
    '''
    Задание 15.4a

    Создать функцию convert_to_dict, которая ожидает два аргумента:
    * список с названиями полей
    * список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 15.4

    Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
    [{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
     {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

    Проверить работу функции на примере файла sh_ip_int_br_2.txt:
    * первый аргумент - список headers
    * второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

    Функцию parse_sh_ip_int_br не нужно копировать.
    Надо импортировать или саму функцию, и использовать то же регулярное выражение,
    что и в задании 15.4, или импортировать результат выполнения функции parse_show.

    Ограничение: Все задания надо выполнять используя только пройденные темы.

    '''
    
    regex = '(\S+\d)\s+(\S+).*(up|admin\S+\s\S+)\s+(\S+)'
    with open(file_name, "r") as f:
        return [re.search(regex, line).groups() for line in f if re.search(regex, line)]


def convert_to_dict(list_name, list_val):
    list_dict = []
    for k, v in enumerate(list_val):
        list_dict.append(dict(zip(headers, list_val[k])))
    return list_dict 

print(convert_to_dict(headers, parse_sh_ip_int_br(args.file_name)))
