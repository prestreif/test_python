#!/usr/bin/env python3.6

with open("CAM_table.txt", "r") as in_file:
    for line in in_file:
        if line.find("Gi0/") != -1:
            print("{0:<5} {1:<15} {3:<5}".format(*(line.split())))
            #print(line.split())
