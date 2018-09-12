#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from draw_network_graph import *
from task_11_1 import *
from sys import argv

'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

def read_file(file_name):
    with open(file_name, "r") as f:
       return parse_cdp_neighbors(f.read())
       #print(f.read())

def create_dict_in_file(*in_files):
    '''
    Create dict for to file
    '''
    dict_graph = dict()
    for in_file in in_files:
        #print(in_file)
        #print(read_file(in_file))
        dict_graph.update(read_file(in_file))
    
    return dict_graph

draw_topology(create_dict_in_file(*argv[1:]), "swg_11_2a")
