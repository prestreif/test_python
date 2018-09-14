#!/usr/bin/env python3.6

from sys import argv
import subprocess
import ipaddress
import pprint

def ping(ip):
    '''
    ping only IP address and retrurn dictinary
    tuple = ["IP" [True|False]]
    '''

    reply =  subprocess.run('ping {ip} -c 3'.format(ip = ip), shell = True, 
            stdout = subprocess.DEVNULL, 
            stderr = subprocess.DEVNULL)

    if reply.returncode == 0:
        return str(ip), True
    else:
        return str(ip), False


def ip_to_network(ip_addr, wild_card_pref):
    '''
    return object ipaddress.ip_network
    '''
    print(ip_addr + " " + str(32 - wild_card_pref))

    return ipaddress.ip_network(
            ".".join(str(str_i) for str_i in
                list(
                    int(
                        ("{:08b}{:08b}{:08b}{:08b}".format(*list(int(val) for val in ip_addr.split(".")))[:32-wild_card_pref] + "0" * wild_card_pref)[i:i+8],
                        2)
                    for i in range(0, 32, 8))
                )
        + "/" +  str(32 - wild_card_pref))

def get_list_ip(ip_addr):
    ip_addr = ip_addr.strip().split()
    if len(ip_addr) > 1:
        wild_card_pref = "{:08b}{:08b}{:08b}{:08b}".format(*list(int(val) for val in ip_addr[1].split(".")))[::-1].index("1")
        ip_network = ip_to_network(ip_addr[0], wild_card_pref)
    elif '/' in ip_addr[0]:
        ip_addr = ip_addr[0].split("/")
        ip_network = ip_to_network(ip_addr[0], 32 - int(ip_addr[1]))
    else:
        ip_network = ip_to_network(ip_addr[0], 6)

    return list(ip_network.hosts())

def check_ip_addresses(*list_ip):
    ip_list = {True: list(), False: list()}
    i = 0;
    max_i = len(list_ip)
    for ip in list_ip:
        ip_reply = ping(ip)
        ip_list[ip_reply[1]].append(ip_reply[0])
        i+=1
        print("Проверен {} из {}".format(i, max_i))
    
    pprint.pprint(ip_list)




check_ip_addresses(*get_list_ip(argv[1]))
