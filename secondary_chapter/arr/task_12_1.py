#!/usr/bin/env python3.6

from sys import argv
import subprocess
import ipaddress
import tabulate

def ping(ip):
    '''
    ping only IP address and retrurn dictinary
    tuple = ["IP" [True|False]]
    '''

    reply =  subprocess.run('ping {ip} -c 3'.format(ip = ip), shell = True, 
            stdout = subprocess.DEVNULL, 
            stderr = subprocess.DEVNULL)

    if reply.returncode == 0:
        return ip, True
    else:
        return ip, False


def ip_to_network(ip_addr, count_pref):
    '''
    return object ipaddress.ip_network
    '''
    #print(ip_addr + " " + str(count_pref))
    return ipaddress.ip_network(
            ".".join(str(str_i) for str_i in
                list(
                    int(
                        ("{:08b}{:08b}{:08b}{:08b}".format(*list(int(val) for val in ip_addr.split(".")))[:32-count_pref] + "0" * count_pref)[i:i+8],
                        2)
                    for i in range(0, 32, 8))
                ) + "/" + str(32 - count_pref)
            )

def parse_ip_str(ip_str):
    list_ip = list()
    if '-' in ip_str:
        ip_str = ip_str.split('-')
        start_ip = ip_str[0].split('.')[::-1]
        end_ip = ip_str[1].split('.')[::-1]
        end_ip = ".".join((end_ip + list(val for key, val in enumerate(start_ip) if not key < len(end_ip)))[::-1]) 
        start_ip =  ipaddress.ip_address(".".join(start_ip[::-1]))
        end_ip = ipaddress.ip_address(end_ip)
        if start_ip > end_ip:
            temp_ip = start_ip
            start_ip = end_ip
            end_ip = temp_ip
        #print(str(ipaddress.ip_address(start_ip)) + " => " + str(ipaddress.ip_address(end_ip))) 
        return list(str(ipaddress.ip_address(ip)) for ip in range(int(start_ip), int(end_ip) + 1))
    else:
        return [ip_str]


def get_list_ip(in_ip_addr):
    ip_addr = in_ip_addr.strip().split()
    if len(ip_addr) > 1:
        count_pref = "{:08b}{:08b}{:08b}{:08b}".format(*list(int(val) for val in ip_addr[1].split(".")))[::-1].index("1")
        ip_network = ip_to_network(ip_addr[0], count_pref)
        print(ip_network)
    elif '/' in in_ip_addr:
        ip_addr = in_ip_addr.split("/")
        ip_network = ip_to_network(ip_addr[0], 32 - int(ip_addr[1]))
        print(ip_network)
    else:
       return parse_ip_str(in_ip_addr)

    return ip_network.hosts()

def check_ip_addresses(*list_ip):
    #print(list_ip)
    reply_list = {True: [], False: []}
    for ip in list_ip:
        i = ping(ip)
        reply_list[i[1]].append(i[0])
    print(tabulate.tabulate(reply_list, headers="keys"))

check_ip_addresses(*get_list_ip(argv[1]))
#parse_ip_str(argv[1])
