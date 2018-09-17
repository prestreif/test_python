#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sys import argv
import re
import argparse

parser = argparse.ArgumentParser(description='Получить список интерфейс => IP, MCASK')

parser.add_argument('file_name', action="store", help="конфигурационный файл")

args = parser.parse_args()

def parse_cfg(file_name):
    '''
    Задание 15.3a

    Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
    * ключ: имя интерфейса
    * значение: кортеж с двумя строками:
      * IP-адрес
      * маска

    Например (взяты произвольные адреса):
    {'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
     'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

    Для получения такого результата, используйте регулярные выражения.

    Проверить работу функции на примере файла config_r1.txt.

    Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
    диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

    '''

    regex_intf = '^interface\s(\S+)'
    regex_ip = '((?:\d+\.){3}(?:\d+)) ((?:\d+\.){3}(?:\d+))'

    
    intf = False
    dict_ip_mask = dict()

    with open(file_name, "r") as f:
        for line in f:
            if line.startswith("!"):
                intf = False;
                continue;
            elif not intf and re.search(regex_intf, line):
                intf = re.search(regex_intf, line).group(1)
            elif intf and re.search(regex_ip, line):
                dict_ip_mask.setdefault(intf, list())
                dict_ip_mask[intf].append(re.search(regex_ip, line).groups())


    return dict_ip_mask

print(parse_cfg(args.file_name))
