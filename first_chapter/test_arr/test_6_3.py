#!/usr/bin/env python3.6

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
print('*' * 30)

for intf in fast_int["trunk"]:
    print('interface FastEthernet {}'.format(intf))
    for command in trunk_template:
        if(command.endswith('vlan')):
            if fast_int['trunk'][intf][0] == "add":
                print("  {} add {}".format(command, ",".join(fast_int['trunk'][intf][1:])))
            elif fast_int['trunk'][intf][0] == "del":
                print("  {} remove {}".format(command,  ",".join(fast_int['trunk'][intf][1:])))
            else:
                print("  {} {}".format(command,  ",".join(fast_int['trunk'][intf][1:])))

        else:
            print('  {}'.format(command))
