#!/usr/bin/env python3.6

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']


dict_mod_inf = dict(access = "VLAN number", trunk = "allowed VLANs") 

mod_intf = input("Enter interface mode (access/trunk): ")
intf = input("Enter interface type and number: ")

vlans = input("Enter {}: ".format(dict_mod_inf[mod_intf]))

templats = dict(access = access_template, trunk = trunk_template)

print("interface {}".format(intf))
print(("\n".join(templats[mod_intf])).format(vlans))
