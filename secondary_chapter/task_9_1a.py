#!/usr/bin/env python3.6

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }


def generate_access_config(psecurity = False, **kwargs):
    '''
     access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    
    access_template = [
                    'interface {}',
                    '\tswitchport mode access',
                    '\tswitchport access vlan {}',
                    '\tswitchport nonegotiate',
                    '\tspanning-tree portfast',
                    '\tspanning-tree bpduguard enable']
    
    port_security = ['\tswitchport port-security maximum 2',
                     '\tswitchport port-security violation restrict',
                     '\tswitchport port-security']

    for key, val in kwargs.items():
        print("\n".join(access_template).format(key,val))
        if psecurity == True:
            print("\n".join(port_security))
        print('!');

generate_access_config(**access_dict, psecurity = True)
