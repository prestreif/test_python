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

    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    
    access_template = [
                    '\tswitchport mode access',
                    '\tswitchport access vlan {}',
                    '\tswitchport nonegotiate',
                    '\tspanning-tree portfast',
                    '\tspanning-tree bpduguard enable']
    
    port_security = ['\tswitchport port-security maximum 2',
                     '\tswitchport port-security violation restrict',
                     '\tswitchport port-security']

    if psecurity == True:
        access_template.extend(port_security)

    return {intf: "\n".join(access_template).format(vlan) for intf, vlan in kwargs.items()}

for key, val in  generate_access_config(**access_dict, psecurity = True).items():
    print(key)
    print(val)
    print('*' * 20)

