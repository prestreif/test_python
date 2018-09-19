#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from draw_network_graph import draw_topology
from task_17_2b import generate_topology_from_cdp
import argparse
import glob
from pprint import pprint


'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

def complite_topology_cdp(dict_topology):
    
    #{('R4', 'Eth0/1'): ('R5', 'Eth0/1'),
    #('R4', 'Eth0/2'): ('R6', 'Eth0/0')}
    
    #'R6': {'Eth 0/1': {'R2': 'Eth 0/2'}},

    dict_test = dict()
    for key, val in dict_topology.items():
        for sub_key, sub_val in val.items():
            dict_test[(key, sub_key)] = tuple(*sub_val.items())

    pprint(dict_test)
    draw_topology(dict_test)

    #pprint({key: sub_val for key, val in dict_topology.items() for sub_val in val.keys()})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "API для создания топологии")

    parser.add_argument("regex_file", action="store", help="(regex)Шаблон для выбора файлов с выводом show cdp neigbor")
    
    args = parser.parse_args()
    
    complite_topology_cdp(generate_topology_from_cdp(glob.glob(args.regex_file))) 
