#!/usr/bin/env python3.6

from sys import argv
import re
import argparse

parser = argparse.ArgumentParser(description="Поиск в тексте по регулярному вырожению")
parser.add_argument('file_name', action="store", help="Название файла с текстом")
parser.add_argument('regex', action="store", help="Регулярное вырожение")

args = parser.parse_args()

def preint_file_with_regex(file_name, regex):
    with open(file_name, "r") as f:
        for line in f:
            if re.search(regex, line):
                print(line, end='')

preint_file_with_regex(args.file_name, args.regex)
