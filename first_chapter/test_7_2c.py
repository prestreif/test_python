#!/usr/bin/env python3.6

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

try:
    in_file = argv[1]
except:
    print("Укажите файл при запуске скрипта !")
    raise SystemExit(0)

try:
    out_file = argv[2]
except:
    print("Укажите выходной файл")
    raise SystemExit(0)

try:
    with open(in_file, "r") as op_file, open(out_file, "w") as wr_file :
        for line in op_file:
            if not line.startswith("Current configuration") and not set(line.split())&set(ignore):
                wr_file.write(line)
except IOError:
    print("Указан не существующий файл")

