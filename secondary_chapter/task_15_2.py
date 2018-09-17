#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sys import argv
import re
import argparse

parser = argparse.ArgumentParser(description="Поиск в тексте по регулярному вырожению")
parser.add_argument('file_name', action="store", help="Название файла с текстом")
parser.add_argument('regex', action="store", help="Регулярное вырожение")

args = parser.parse_args()

def preint_file_with_regex(file_name, regex):
    '''
    Задание 15.2

    Создать функцию return_match, которая ожидает два аргумента:
    * имя файла, в котором находится вывод команды show
    * регулярное выражение

    Функция должна обрабатывать вывод команды show построчно и возвращать список подстрок,
    которые совпали с регулярным выражением (не всю строку, где было найдено совпадение,
    а только ту подстроку, которая совпала с выражением).

    Проверить работу функции на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
    Вывести список всех IP-адресов из вывода команды.

    Соответственно, регулярное выражение должно описывать подстроку с IP-адресом (то есть, совпадением должен быть IP-адрес).


    Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
    диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

    '''
    with open(file_name, "r") as f:
        return list(re.search(regex, line).group() for line in f if re.search(regex, line))


print(preint_file_with_regex(args.file_name, args.regex))

