#!/usr/bin/env python3.6

import argparse
import subprocess

def ping(ip_addr, count):
    '''
    ping only ip address specifid number of times
    and return tuple
    
    On success: (return code = 0, command output)
    On failure: (return code, error output (stderr))
    '''
    reply = subprocess.run('ping -c {count} -n {ip}'
            .format(ip = ip_addr, count = count),
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            encoding = "utf-8")

    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr

parser = argparse.ArgumentParser(description="Ping script")

parser.add_argument("ip", action="store", help="destination ip address")
parser.add_argument("-c", action="store", help="number of ICMP packets", dest="count", default=2, type=int)

args = parser.parse_args()

print(args)

rc, msg = ping(args.ip, args.count)
print(msg)

