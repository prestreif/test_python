#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sys import argv
import glob
import argparse
from task_17_2a import *
from pprint import pprint
'''
Задание 17.2b

Переделать функциональность скрипта из задания 17.2a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 17.2a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''
def generate_topology_from_cdp(list_of_files, save_to_file = True, topology_filename = "topology.yaml"):
    if len(list_of_files) < 1:
        print('*' * 30)
        print("Не найдено файлов для вывода")
        print('*' * 30)
        return
    else:
        print('-' * 30)
        print("Выбранные файлы: ", end='\n ')
        print("\n ".join(list_of_files))
        print("-" * 30)

    dict_cdp = create_dict_cdp([parse_sh_cdp_neighbors(read_file(ifile)) for ifile in list_of_files])
    
    if save_to_file:
        with open(topology_filename, "w") as f:
            yaml.dump(dict_cdp, f)

        print("Запись результата в файл => {}".format(topology_filename))

    return dict_cdp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Парсер sh cdp neighbor")

    parser.add_argument('regex_files', action="store", help="Регулярное вырожение для загрузки всех файлов")
    parser.add_argument('-s', action="store", dest='save_to_file', help="[True|False] Сохранить в файл", default="True")
    parser.add_argument('-f', action="store", dest='file_name', help="Название файла в который производится сохранение", default="topology.yaml")

    args = parser.parse_args()
    generate_topology_from_cdp(glob.glob(args.regex_files), args.save_to_file, args.file_name)
