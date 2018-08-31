#!/usr/bin/env python3.6

ip, pref = (input("Введите ip/iprefix: ")).split('/')

ip = ip.split('.')

ip = [int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])]

netmask = ("{:032b}".format(int(('1' * int(pref)), 2))) 

netmask = [int(netmask[32:23:-1], 2), int(netmask[23:15:-1],2), int(netmask[15:7:-1],2), int(netmask[7::-1],2)]

print("Network: \n\n{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}\n".format(*ip))
print("Mask: \n/{:<8}".format(pref))
print("{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}".format(*netmask))
