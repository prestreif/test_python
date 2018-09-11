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

def result_comm_file(files = "config_sw1.txt"):
    '''
    Функция проходится по текстовому файлу конфигурации
    и возвращает словарь команд в файле.

    Все коментарии (начало строки с !) и команды в которых из списка ignore
    в вывод не попадают
    '''
    command_key = ""
    dict_command = dict()
    with open(files, "r") as f:
        for line in f:
            if line.startswith("!") or ignore_command(line, ignore) or line.startswith("\n"):
                continue
            if not line.startswith(" ") and  not line.startswith("\t"):
                command_key = line.strip()
                dict_command[command_key] = []
            elif command_key:
                dict_command[command_key].append(line.strip())
    return dict_command



dict_command = result_comm_file(argv[1]) if len(argv) >= 2  else result_comm_file(input("Введите название файла: "))
print('*' * 10 + "конфиг файла" + '*' * 10)
print("\n".join(str(command) + "\n  " + "\n  ".join(values) for command, values in dict_command.items()))
