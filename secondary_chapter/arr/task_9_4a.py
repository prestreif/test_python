#!/usr/bin/env python3.6

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)

def add_command_in_dict(lines):
    #print(lines)
    dict_comm = dict()
    key = ""
    subkey = ""
    for line in lines:
        if not line.startswith(" "):
            key = line.strip()
            dict_comm[key] = {}
        elif line.startswith("  "):
            dict_comm[key][subkey].append(line.strip())
        else:
            subkey = line.strip()
            dict_comm[key][subkey] = []
     
    return dict_comm


def result_comm_file(files = "config_sw1.txt"):
    '''
    Функция проходится по текстовому файлу конфигурации
    и возвращает словарь команд в файле.

    Все коментарии (начало строки с !) и команды в которых из списка ignore
    в вывод не попадают
    '''
    
    lines = []

    with open(files, "r") as f:
        for line in f:
            if "!" in line or ignore_command(line, ignore):
                continue
            else:
                lines.append(line.rstrip(" \n"))
    
    return add_command_in_dict(lines)


dict_command = result_comm_file(argv[1]) if len(argv) >= 2  else result_comm_file(input("Введите название файла: "))
#print(dict_command)
#print('*' * 10 + "конфиг файла" + '*' * 10)
for key, val in dict_command.items():
    print(key)
    #print(val)
    if type(val) == dict:
        for sub_key, sub_val in val.items():
            print("{}\n{}".format("  " + str(sub_key), "".join("    " + str(v) + "\n" for v in sub_val)), end='')

