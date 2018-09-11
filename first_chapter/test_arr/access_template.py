#!/usr/bin/env python3.6
#from sys import argv

#interface, vlan = argv[1:]

interface = input("Введите желаемый интерфейс: ")
vlan = input("Какой Vlan будем на него вешать?\nНомер Vlan: ")

access_template=['switchport mode access',
                 'switchport access vlan {}',
                 'switchport nonegotiate',
                 'spanning-three portfast',
                 'spanning-three bpduguard enable']
print("\n" + "#"*30)
print("\nInterface {}".format(interface))
print("\n".join(access_template).format(vlan))
print("\n" + "#"*30)
