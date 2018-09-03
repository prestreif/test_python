#!/usr/bin/env python3.6

from sys import argv

try:
    in_file = argv[1]
except:
    print("Укажите файл при запуске скрипта !")
    raise SystemExit(0)

try:
    with open(in_file, "r") as op_file:
        for line in op_file:
            if not line.startswith("!"):
                print(line, end='')
except IOError:
    print("Указан не существующий файл")

