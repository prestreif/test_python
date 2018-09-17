#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re
import argparse
from sys import argv

parser = argparse.ArgumentParser(description="parser 'sh ip int br' with file_name")

parser.add_argument('file_name', action="store", help="file_name with output command sh ip int br")

args = parser.parse_args()

def parse_sh_ip_int_br(file_name):

    '''
    Задание 15.4

    Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
    имя файла, в котором находится вывод команды show

    Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
    * Interface
    * IP-Address
    * Status
    * Protocol

    Информация должна возвращаться в виде списка кортежей:
    [('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
     ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
     ('FastEthernet0/2', 'unassigned', 'up', 'up')]

    Для получения такого результата, используйте регулярные выражения.

    Проверить работу функции на примере файла sh_ip_int_br_2.txt.

    '''
    regex = '(\S+\d)\s+(\S+).*(up|admin\S+\s\S+)\s+(\S+)'
    with open(file_name, "r") as f:
        return [re.search(regex, line).groups() for line in f if re.search(regex, line)]

print(parse_sh_ip_int_br(args.file_name))
