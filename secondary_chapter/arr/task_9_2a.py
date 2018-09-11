#!/usr/bin/env python3.6


trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

def generate_trunk_config(**trunk):
    '''
        trunk - словарь trunk-портов,
        для которых необходимо сгенерировать конфигурацию, вида:
            { 'FastEthernet0/1':[10,20],
            'FastEthernet0/2':[11,30],
            'FastEthernet0/4':[17] }

        Возвращает словарь:
        - ключи: имена интерфейсов, вида 'FastEthernet0/1'
        - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan {}']
    
    dict_intf = {intf: ("\n".join("\t" + command for command in trunk_template).format(",".join(str(vlan) for vlan in vlans) + "\n"))
            for intf, vlans in trunk_dict.items()
            }

    #command_intf = ""
    #for intf, vlans in trunk_dict.items():
    #   command_intf += "interface {}\n".format(intf) + "\n".join("\t" + command for command in trunk_template).format(",".join(str(vlan) for vlan in vlans) + "\n")

    return dict_intf
print("".join(string + val for string, val in generate_trunk_config(**trunk_dict).items()))
