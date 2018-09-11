#!/usr/bin/python3.6

from sys import argv

def get_int_vlan_map(name_file):
    '''
        Получить из конфигурационного файла порты и их вланы
        выдает словарь с trunk и access 
    '''

    dict_intf = dict()
    intf = ""
    access = False

    with open(name_file, "r") as f:
        for line in f:
            if "interface" in line:
                if intf and dict_intf.get("trunk") != None and dict_intf["trunk"].get(intf) == None:
                    if access:
                        dict_intf.setdefault("access", {})
                        dict_intf["access"][intf] = 1
                    else:
                        dict_intf.setdefault("unknoun", {})
                        dict_intf["unknoun"][intf] = ""
                intf = line.split()[-1]
                access = False
            elif "allowed vlan" in line:
                dict_intf.setdefault("trunk", {})
                dict_intf["trunk"][intf] = [int(vlan) for vlan in line.split()[-1].split(',')]
            elif "access vlan" in line:
                dict_intf.setdefault("access", {})
                dict_intf["access"][intf] = int(line.split()[-1])
            elif "mode access" in line:
                access = True


    return dict_intf

while 1:
    dict_intf = get_int_vlan_map(argv[1])
    #print(dict_intf)
    m = input("Введите режим работы порта {}:".format(",".join(dict_intf.keys())))
    if  m in "accessitrunkunknoun":
        print("".join(str(key) + " => "  + str(val) + "\n" for key, val in  dict_intf[m].items()))
    else:
        break;
