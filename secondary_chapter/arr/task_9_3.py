#!/usr/bin/python3.6

from sys import argv

def get_int_vlan_map(name_file):
    '''
        Получить из конфигурационного файла порты и их вланы
        выдает словарь с trunk и access 
    '''

    dict_intf = dict()
    intf = ""
    with open(name_file, "r") as f:
        for line in f:
            if "interface" in line:
               intf = line.split()[-1]
            elif "allowed vlan" in line:
                dict_intf.setdefault("trunk", {})
                dict_intf["trunk"][intf] = [int(vlan) for vlan in line.split()[-1].split(',')]
            elif "access vlan" in line:
                dict_intf.setdefault("access", {})
                dict_intf["access"][intf] = int(line.split()[-1])

    return dict_intf

while 1:
    dict_intf = get_int_vlan_map("config_sw1.txt")
    #print(dict_intf)
    m = input("Введите режим работы порта {}:".format(",".join(dict_intf.keys())))
    if "trunk" in m or "access" in m:
        print("".join(str(key) + " => "  + str(val) + "\n" for key, val in  dict_intf[m].items()))
    else:
        break;
