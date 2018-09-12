#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sys import argv

def parse_cdp_neighbors(in_str):
    """
    Задание 11.1

    Создать функцию parse_cdp_neighbors, которая обрабатывает
    вывод команды show cdp neighbors.

    Функция ожидает, как аргумент, вывод команды одной строкой.

    Функция должна возвращать словарь, который описывает соединения между устройствами.

    Например, если как аргумент был передан такой вывод:
    R4>show cdp neighbors

    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0

    Функция должна вернуть такой словарь:

        {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
        ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

    Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

    Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

    Ограничение: Все задания надо выполнять используя только пройденные темы.
    """

    in_line = list(val.strip() for val in in_str.strip().split('\n') if val.strip().startswith("R") or val.strip().startswith("SW"))
    return  {
            (in_line[0][0:in_line[0].find(">")], #the first part of the dictionary key, in first line in the text search name network device
                "".join(line.strip().split()[1:3])): #the secondary of the part dictionary key, in other lines search Local Interface
            (line.strip().split()[0], "".join(line.strip().split()[-2:])) #the value of the dictionary, serach in line first and last name and interface
            for line in in_line[1:]}


if __name__ == '__main__':
    print(argv)
    print(parse_cdp_neighbors(argv[1]))
