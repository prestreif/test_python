#!/usr/bin/env python3.6

lines = []

with open("CAM_table.txt", "r") as in_file:
    for line in in_file:
        if line.find("Gi0/") != -1:
            lines.append(line.split())


lines.sort()
for line in lines:
    print("{0:<5} {1:<15} {3:<5}".format(*line))
            #print(line.split())
