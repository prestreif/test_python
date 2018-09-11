#!/usr/bin/env python3.6

ospf_lines = ""

try:
    f = open("ospf.txt", "r")
    ospf_lines = f.readlines()
except:
    print("Ошибка при открытии файла")
finally:
    f.close()

lines = '''
        Protocol:           {0}
        Prefix:             {1}
        AD/Metric:          {2}
        Next-Hop:           {4}
        Last update:        {5}
        Outbound Interface: {6}   
'''



for line in ospf_lines:
    line = line.replace(",[]", "").replace("O", "OSPF")
    line = line.strip().split() 
    print("*" * 20)
    print(lines.format(*line))
    print("*" * 20)

