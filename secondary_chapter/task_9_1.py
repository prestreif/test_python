#!/usr/bin/env python3.6

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }


def generate_access_config(**kwargs):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    
    access_template = [
                    'interface {}',
                    'switchport mode access',
                    'switchport access vlan {}',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']
    
    for key, val in kwargs.items():
        print("\n".join(access_template).format(key,val))
        print('!');

generate_access_config(**access_dict)
