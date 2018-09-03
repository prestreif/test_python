#!/usr/bin/env python3.6

lines = dict()

with open("CAM_table.txt", "r") as in_file:
    for line in in_file:
        if line.find("Gi0/") != -1:
            r_vid = line.split()
            if lines.get(r_vid[0]) == None:
                lines[r_vid[0]] = list()
            
            lines[r_vid[0]].append(r_vid)
            


#print(lines)

while 1:
    print("*" * 40)
    print("Введите любой символ кроме цифры для выхода из программы.")
    m = input("Введите номер vlan для вывода: ")
    if m.isdigit():
        #print(lines[m])
        for line in lines[m]:
            print("{0:<5} {1:<15} {3:<5}".format(*line))
            #print(line)
    else:
        break
